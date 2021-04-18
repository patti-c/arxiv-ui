from flask import Flask, jsonify, request
import requests
import feedparser
from .util.decorators import handles_exceptions_gracefully
from .util.constants import ARXIV_BULK_URL_BASE, ARTICLES_SEARCH, INDEX_TEXT, ARXIV_BASIC_URL_BASE
from time import sleep
from dateutil import parser
from datetime import datetime
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def index():
    return INDEX_TEXT


@handles_exceptions_gracefully
@app.route('/api/v1/resources/articles')
@cross_origin(supports_credentials=True)
def articles():
    payload = {
              'start': 0,
              'max_results': 10,
              'sortBy': 'submittedDate',
              'sortOrder': 'ascending'}
    entries = arxiv_fetch(ARXIV_BULK_URL_BASE + ARTICLES_SEARCH, params=payload).get('entries', [])
    formatted_entries = format_articles(entries)
    return jsonify(formatted_entries)


def format_articles(entries):
    # Strips out data that the front end doesn't need.
    return [filter_out_undesired_keys(entry, ('author', 'authors', 'summary', 'title')) for entry in entries]


def filter_out_undesired_keys(d, desired_keys):
    return {key: d[key] for key in desired_keys}


@handles_exceptions_gracefully
@app.route('/api/v1/resources/authors')
@cross_origin(supports_credentials=True)
def authors():
    author_name = request.args.get('name')
    if author_name:
        return fetch_author(author_name)
    else:
        return fetch_authors()


def fetch_authors():
    payload = {
        'start': 0,
        'max_results': 10,
        'sortBy': 'submittedDate',
        'sortOrder': 'ascending'}
    articles_data = arxiv_fetch(ARXIV_BULK_URL_BASE + ARTICLES_SEARCH, payload)
    authors_data = {article['author']: None for article in articles_data['entries']}
    for author in authors_data.keys():
        authors_data[author] = fetch_author(author)
    return jsonify(authors_data)


def fetch_author(author_name) -> dict:
    payload = {
              'start': 0,
              'max_results': 100,
              'sortBy': 'submittedDate',
              'sortOrder': 'ascending'}
    formatted_author_name = author_name.replace(' ', '+')
    author_data = arxiv_fetch(ARXIV_BULK_URL_BASE + f'?search_query=au:{formatted_author_name}', params=payload)
    entries = filter_out_authors_with_similar_names(author_name, author_data['entries'])
    author_data['mostRecentArticle'] = get_most_recent_article_date(entries).isoformat()
    author_data['articlesInLastSixMonthsCount'] = get_articles_in_last_six_months_count(entries)
    return author_data


def sanitize_author_name(author_name: str) -> str:
    # Pretty sure it's actually a little more complicated than this but this is good enough for the moment.
    # probably a urllib helper for this?
    return author_name.replace(' ', '+')


def filter_out_authors_with_similar_names(author_name: str, entries: list) -> list:
    # Sometimes the API returns articles for an author with a very similar name;
    # our API is going to be a little more strict and only return exact hits.
    return [entry for entry in entries if entry['author'] == author_name]


def get_most_recent_article_date(entries: list) -> datetime:
    return max([article_published_datetime(article) for article in entries])


def article_published_datetime(article) -> datetime:
    return parser.isoparse(article['published'])


def get_articles_in_last_six_months_count(entries: list) -> int:
    return len([article for article in entries if
                difference_in_months_between(article_published_datetime(article), datetime.now()) > 6])


def difference_in_months_between(start_date, end_date) -> int:
    return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


def arxiv_fetch(url: str, params: dict) -> dict:
    # We're going to be polite with arxiv but not *that* polite
    sleep(.5)
    data = requests.get(url, params=params)
    return feedparser.parse(data.content)


app.run()

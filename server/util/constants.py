ARXIV_BULK_URL_BASE = 'http://export.arxiv.org/api/query/'
ARXIV_BASIC_URL_BASE = 'http://arxiv.org/'
INDEX_TEXT = '''<h1>arXiv Article Fetcher</h1>
    <p>A prototype API for fetching articles about the intersection of computing and psychiatry.</p>'''
RELEVANT_CATEGORIES = 'all:psychiatry+OR+all:therapy+OR+all:machine+learning+OR+all:data+science'
ARTICLES_SEARCH = f'?search_query={RELEVANT_CATEGORIES}'

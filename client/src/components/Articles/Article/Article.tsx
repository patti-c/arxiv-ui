import React from 'react';
import './Article.css'

const Article = (article: any) => {
	const displayAuthors = (primaryAuthor: string, allAuthors: [any]) => {
		const nonPrimaryAuthors = allAuthors.filter(author => author['name'] != primaryAuthor).map(author => author['name']);
		if (nonPrimaryAuthors.length) {
			return `${primaryAuthor} and ${nonPrimaryAuthors.join(', ')}`
		} else {
			return primaryAuthor;
		}
	};

	return (
		<li className="articleListItem">
			<h3>{article['title']} by {displayAuthors(article['author'], article['authors'])}</h3>
			<p>{article['summary']}</p>
		</li>
	)
};

export default Article

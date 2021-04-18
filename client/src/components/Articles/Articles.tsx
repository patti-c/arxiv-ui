import React, { useState, useEffect } from 'react';
import './Articles.css'
import Article from './Article/Article';

function Articles() {

	const [articles, setArticles] = useState([]);

	useEffect( () => {
		fetch('http://localhost:5000/api/v1/resources/articles')
			.then(resp => resp.json())
			.then(setArticles)
	}, []);

	return (
		<div>
			<h1 style={{"textAlign": "center"}}>Articles</h1>
			<ul>
				{articles.map((article: any) => <Article {...article}/>)}
			</ul>
		</div>)
}

export default Articles

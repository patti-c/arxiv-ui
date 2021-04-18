import React from 'react';
import logo from '../../assets/arxiv.png';
import './Home.css'
import {
	Link
} from 'react-router-dom';


function Home() {
	return (
		<div className="Home">
			<header className="Home-header">
				<img src={logo} className="Home-logo" alt="logo" />
				<ul className="links-list">
					<li>
						<Link to="/articles">View Articles</Link>
					</li>
					<li>
						<Link to="/authors">View Authors</Link>
					</li>
				</ul>
			</header>
		</div>
	)
}

export default Home

import React from 'react';
import './App.css';
import { Home, Articles, Authors } from './components'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from 'react-router-dom';
import home from './assets/home.png';

function App() {
  return (
      <Router>
          <Link to="/">
              <img style={{height: '2em', margin: '.5em'}} src={home} alt="home-icon"/>
          </Link>
        <Switch>
            <Route exact path="/">
                <Home/>
            </Route>
            <Route exact path="/articles">
                <Articles/>
            </Route>
            <Route exact path="/authors">
                <Authors/>
            </Route>
        </Switch>
      </Router>
  );
}

export default App;

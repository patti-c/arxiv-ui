import React from 'react';
import './App.css';
import { Home, Articles, Authors } from './components'
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom';

function App() {
  return (
      <Router>
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

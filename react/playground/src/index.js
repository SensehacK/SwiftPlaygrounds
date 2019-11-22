import React from 'react';
import ReactDOM from 'react-dom';
import "bootstrap/dist/css/bootstrap.css";
// import App from './App.js'
import MainApp from './sense_blog/mainApp'
// import 'font-awesome/css/font-awesome.min.css';

// CSS
import './css/App.css';

const element = <h1>Hello SensehacK!</h1>

/* Earlier Counters App code, 
didn't want to create a new Repo for React assignment
 as I would indirectly move this codebase to my main repo for easy structure
 Link : https://github.com/SensehacK/masters_comp_science
 */
// ReactDOM.render(<App />, document.getElementById('root'));

// Internet Computing Assignment 4
ReactDOM.render(<MainApp />, document.getElementById('root'));

console.log('Kautilya ? Sensehack : L');

console.log(element);

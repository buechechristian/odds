'use strict';

process.env.DEBUG = 'actions-on-google:*';
const App = require('actions-on-google').ApiAiApp;
const functions = require('firebase-functions');


// a. the action name from the make_name API.AI intent
const NAME_ACTION = 'make_name';
// b. the parameters that are parsed from the make_name intent 
const COLOR_ARGUMENT = 'color';
const NUMBER_ARGUMENT = 'number';


exports.sillyNameMaker = functions.https.onRequest((request, response) => {
  const app = new App({request, response});
  console.log('Request headers: ' + JSON.stringify(request.headers));
  console.log('Request body: ' + JSON.stringify(request.body));


// c. The function that generates the silly name
  function makeName (app) {
    let number = app.getArgument(NUMBER_ARGUMENT);
    let color = app.getArgument(COLOR_ARGUMENT);
    app.tell('Alright, your silly name is ' +
      color + ' ' + number +
      '! I hope you like it. See you next time.');
  }
  // d. build an action map, which maps intent names to functions
  let actionMap = new Map();
  actionMap.set(NAME_ACTION, makeName);


app.handleRequest(actionMap);
});
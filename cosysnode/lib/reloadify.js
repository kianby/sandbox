"use strict";

var sendevent = require('sendevent');
var watch = require('watch');
var ENV = process.env.NODE_ENV || 'development';

function reloadify(app, dir) {
  if (ENV !== 'development') {
    app.locals.watchScript = '';
    return;
  }

  // create a middlware that handles requests to `/eventstream`
  var events = sendevent('/eventstream');
  app.use(events);
  watch.watchTree(dir, function (f, curr, prev) {
    console.log("=> reload client browser");
    events.broadcast({ msg: 'reload' });
  });

  // assign the script to a local var so it's accessible in the view
  //app.locals.watchScript = '<script>' + script + '</script>';
  app.locals.watchScript = true
}

module.exports = reloadify

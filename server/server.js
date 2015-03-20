/**
 * Module dependencies.
 */

var express = require('express')
  , fs = require('fs');

/**
 * Main application entry file.
 * Please note that the order of loading is important.
 */

process.on('uncaughtException', function(err) {
    console.log(err);
});

// Load configurations
// if test env, load example file
var env = process.env.NODE_ENV || 'development'
  , config = require('./config/config')[env]
  , mongoose = require('mongoose')
  , jwt = require('jsonwebtoken');

// Bootstrap db connection
mongoose.connect(config.db);

// Bootstrap models
var models_path = __dirname + '/app/models'
fs.readdirSync(models_path).forEach(function (file) {
  require(models_path+'/'+file);
});

var app = express();

// authentication
var  auth = require('./config/auth')(app);

// express settings
require('./config/express')(app, config);

// Bootstrap routes
require('./config/routes')(app, auth);

// Start the app by listening on <port>
var port = process.env.PORT || 3000;
app.listen(port);
console.log('Express app started on port '+port);

// expose app
exports = module.exports = app;

/**
 * Module dependencies.
 */

var express = require('express')
  , flash = require('connect-flash')
  , helpers = require('view-helpers')
  , swig = require('swig')
  , compression = require('compression')
  , bodyParser = require('body-parser');

module.exports = function (app, config) {

  app.set('showStackError', true);
  // should be placed before express.static
  app.use(compression({
    filter: function (req, res) {
      return /json|text|javascript|css/.test(res.getHeader('Content-Type'));
    },
    level: 9
  }));
  app.use(express.static(config.root + '/public'));

  // set views path, template engine and default layout
  app.engine('html', swig.renderFile);
  app.set('view engine', 'html');
  app.set('views', config.root + '/app/views');
  app.set('view cache', process.env.NODE_ENV !== 'development');

  // dynamic helpers
  // app.use(function(req,res,next){
  //     req.locals.session = "eeeeeeee";
  //     next();
  // });

  // bodyParser should be above methodOverride
  app.use(bodyParser());

  // connect flash for flash messages
  app.use(flash());

  // assume "not found" in the error msgs
  // is a 404. this is somewhat silly, but
  // valid, you can do whatever you like, set
  // properties, use instanceof etc.
  app.use(function(err, req, res, next){
    // treat as 404
    if (~err.message.indexOf('not found')) return next()

    // log it
    console.error(err.stack)

    // error page
    res.status(500).render('500', { error: err.stack })
  });

  // assume 404 since no middleware responded
  app.use(function(req, res, next){
    res.status(404).render('404', { url: req.originalUrl, error: 'Not found' })
  });

  app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type, Authorization');
    next();
  });
}

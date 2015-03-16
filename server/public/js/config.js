require.config({
    paths: {
      jquery: 'lib/jquery/dist/jquery',
      underscore: 'lib/underscore/underscore',
      backbone: 'lib/backbone/backbone',
      bootstrap: 'lib/bootstrap/dist/js/bootstrap',
      app: 'app'
     }
});

requirejs.onError = function (err) {
  'use strict';
  console.log(err);
  console.log(err.requireType);
  console.log(err.requireModules);
};

require([
  // Load our app module and pass it to our definition function
  'app/tuto',
], function(App){
  // The "app" dependency is passed in as "App"
  App.initialize();
});




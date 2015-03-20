module.exports = function (app, passport, auth) {
  // user routes
  var users = require('../app/controllers/users');
  app.get('/login', users.login);
  app.get('/signup', users.signup);
  app.get('/logout', users.logout);
  app.post('/users', users.create);
  app.get('/users/:userId', users.show);

  // this is home page
  var home = require('../app/controllers/home');
  app.get('/', home.index);
}

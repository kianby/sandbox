var express = require('express');
var router = express.Router();

router.all('/', function (req, res, next) {
  console.log('Enabling CORS ...');
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next() // pass control to the next handler
})

router.get('/', function(req, res, next) {
  res.json(
    {
      "comments": [
      {
        "author": "Bob",
        "site": null,
        "date": "2014-12-21T08:36:38.000Z",
        "gravatar": null,
        "preview": "Du classique mais de la **qualité** !\n\nBonne continuation",
      },
      {
        "author": "Yax",
        "site": "http://www.blogduyax.madyanne.fr",
        "date": "2014-12-21T08:36:38.000Z",
        "gravatar": "308a3596152a79231f3feedc49afa4ef",
        "preview": "Merci ! J'envisage de développer mon propre gestionnaire de …",
      }
      ]
    }
  );
});

module.exports = router;

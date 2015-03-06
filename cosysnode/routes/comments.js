var express = require('express');
var router = express.Router();

router.all('/', function (req, res, next) {
  console.log('Enabling CORS ...');
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next() // pass control to the next handler
})

router.get('/', function(req, res, next) {
  res.json([
    {"nickname":"Yax", "comment":"What's up?"},
    {"nickname":"Bob", "comment":"Silly question"},
    {"nickname":"Yax", "comment":"Nop"} 
  ]);
});


module.exports = router;

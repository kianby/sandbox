#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import controllers
import bottle
from app.bottle.auth_plugin import AuthPlugin

from bottle import run, install
from bottle.ext.mongo import MongoPlugin

from app.controllers import *

# initialize bottle
app = bottle.app()
app.config.load_config("server.conf")
plugin = MongoPlugin(uri="mongodb://" + app.config["mongodb.server"],
                     db=app.config["mongodb.dbname"], json_mongo=True)
install(plugin)
install(AuthPlugin())

bottle.debug(app.config["global.debug"])

run(app=app, host=app.config["http.server"], port=app.config["http.port"])

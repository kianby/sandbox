#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

# add current path and parent path to syspath
currentPath = os.path.dirname(__file__)
parentPath = os.path.abspath(os.path.join(currentPath, os.path.pardir))
paths = [currentPath, parentPath]

for path in paths:
    if path not in sys.path:
        sys.path.insert(0, path)
os.chdir(currentPath)

# import controllers
import config
import bottle
from bottle_preRequest import preRequestPlugin

from bottle import run, install
from bottle.ext.mongo import MongoPlugin

from app.controllers import home
print(home)

# initialize bottle
plugin = MongoPlugin(uri="mongodb://" + config.MONGO_SERVER,
                     db=config.MONGO_DBNAME, json_mongo=True)
install(plugin)
plugin = preRequestPlugin()
install(plugin)

bottle.debug(config.DEBUG)

app = bottle.app()

run(app=app, host=config.HTTP_SERVER, port=config.HTTP_PORT)

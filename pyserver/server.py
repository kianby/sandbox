#!/usr/bin/python
# -*- coding: UTF-8 -*-

# initialize logging
import logging


def configure_logging(level):
    print(level)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    # create formatter
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

# initialize bottle
import bottle
from bottle import run, install
from pymongo import MongoClient

from app.bottle.auth_plugin import AuthPlugin
from app.bottle.inject_plugin import InjectPlugin
from app.factory import Factory

# import controllers
from app.controllers import *

app = bottle.app()
app.config.load_config("server.conf")

# intitialize database
client = MongoClient(app.config["mongodb.server"])
db = client[app.config["mongodb.dbname"]]
app.config['db'] = db
app.config['factory'] = Factory(app)

# TODO move following code elsewhere
if db.users.count() == 0:
    # TODO hash passwords
    db.users.insert({'username': 'admin', 'password': 'admin'})

# load plugins
install(AuthPlugin())
install(InjectPlugin())

# set logging level
debug = app.config['global.debug'].lower() == 'true'
bottle.debug(debug)
logging_level = (20, 10)[debug]
logger = logging.getLogger(__name__)
configure_logging(logging_level)
app.config['logger'] = logger

# start bottle
logger.info('Server started')
run(app=app, host=app.config['http.server'], port=app.config['http.port'])

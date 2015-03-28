#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import logging
import bottle
from bottle import run, install

# add current and parent path to syspath
currentPath = os.path.dirname(__file__)
parentPath = os.path.abspath(os.path.join(currentPath, os.path.pardir))
paths = [currentPath, parentPath]
for path in paths:
    if path not in sys.path:
        sys.path.insert(0, path)

# configure logging

import config

def configure_logging(level):
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    # create formatter
    formatter = logging.Formatter('[%(asctime)s] %(name)s %(levelname)s %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    root_logger.addHandler(ch)

logging_level = (20, 10)[config.DEBUG]
configure_logging(logging_level)

logger = logging.getLogger(__name__)

# initialize database
from app.services import database
database.setup()

# initialize bottle
from app.bottle.auth_plugin import AuthPlugin
from app.bottle.inject_plugin import InjectPlugin
from app.controllers import *

app = bottle.app()

# load plugins
install(AuthPlugin())
install(InjectPlugin())

# set logging level
bottle.debug(config.DEBUG)

# start bottle
if __name__ == '__main__':
    logger.info('Server started')
    run(app=app, host=config.HTTP_SERVER, port=config.HTTP_PORT)

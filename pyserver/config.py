#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

DEBUG = True

ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app")

HTTP_SERVER = "0.0.0.0"
HTTP_PORT = 8080

MONGO_SERVER = "localhost"
MONGO_DBNAME = "cosysnode"

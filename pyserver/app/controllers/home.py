#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bottle import route, redirect
from bson.json_util import dumps


@route('/heartbeat', method='GET')
def heartbeat(mongodb):
    return "alive"


@route('/get', method='GET')
def index(mongodb):
    return dumps(mongodb['collection'].find())


@route('/api', method='GET')
def get_api(mongodb):
    return "OK"


@route('/create', method='POST')
def create(mongodb):
    mongodb['collection'].insert({'a': 1, 'b': 2})
    redirect("/")

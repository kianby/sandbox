#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bottle import route, request, abort
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


def check(username, password):
    return username == 'admin'


@route('/signin', method='POST')
def signin(auth):
    print(auth)
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check(username, password):
        return 'OK'
    else:
        abort(401, 'invalid username or password')

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bottle import route, request, abort


@route('/heartbeat', method='GET')
def heartbeat(logger):
    logger.info('hearbeat level INFO')
    logger.debug('hearbeat level DEBUG')
    return "OK"


@route('/api', method='GET')
def get_api():
    return "1.0"


@route('/login', method='POST')
def login(auth):
    username = request.json.get('username')
    password = request.json.get('password')
    token = auth.login(username, password)
    if token:
        return {'token': token}
    else:
        abort(401, 'invalid username or password')

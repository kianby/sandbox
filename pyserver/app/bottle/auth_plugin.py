#!/usr/bin/python
# -*- coding: UTF-8 -*-

import bottle
from bottle import request


class AuthPlugin(object):

    name = 'auth'
    api = 2

    def __init__(self, keyword='auth', **kwargs):
        self.keyword = keyword

    def setup(self, app):
        pass

    def _checkAuth(self, request):
        return request.get_header('User') and request.get_header('Token')

    def apply(self, callback, context):

        if not context.rule.startswith('/api'):
            return callback

        def wrapper(*args, **kwargs):
            if self._checkAuth(request):
                print("SECURED REQUEST")
                body = callback(*args, **kwargs)
            else:
                print("REJECT REQUEST")
                body = bottle.HTTPError(401, "Unauthorized request")
            return body

        return wrapper

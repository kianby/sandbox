#!/usr/bin/python
# -*- coding: UTF-8 -*-

import bottle
from bottle import request


class AuthPlugin(object):

    name = "auth"
    api = 2

    def __init__(self, keyword='auth', **kwargs):
        self.keyword = keyword
        self.name = "plugin:" + keyword

    def setup(self, app):
        pass

    def _checkAuth(self, request):
        return request.get_header("User") and request.get_header("Token")

    def apply(self, callback, route):

        def wrapper(*args, **kwargs):
            if route.rule.startswith("/api"):
                if self._checkAuth(request):
                    print("SECURED REQUEST")
                    body = callback(*args, **kwargs)
                else:
                    print("REJECT REQUEST")
                    body = bottle.HTTPError(401, "Unauthorized request")
            else:
                body = callback(*args, **kwargs)
            return body

        return wrapper

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import inspect
from bottle import request
from app.factory import Factory


class AuthPlugin(object):

    def __init__(self, keyword='auth', **kwargs):
        self.keyword = keyword
        self.name = "plugin:" + keyword

    def setup(self, app):
        pass

    def apply(self, callback, context):
        args = inspect.getargspec(context['callback'])[0]
        if self.keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            if not request.path.startswith("/api"):
                #
                # Setup session and environment stuff
                #
                request.session = request.environ.get("beaker.session")
                request.all = dict(request.query.items() + request.forms.items())
                request.db = None
                request.factory = Factory(request.db)

                #
                # Finally call the the next method in the chain
                #
                body = callback(*args, **kwargs)

                return body

            else:
                body = callback(*args, **kwargs)
                return body

        return wrapper

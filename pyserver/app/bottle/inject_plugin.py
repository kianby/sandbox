#!/usr/bin/python
# -*- coding: UTF-8 -*-

import inspect


class InjectPlugin(object):

    name = 'inject'
    api = 2

    def __init__(self, keyword='inject', **kwargs):
        self.keyword = keyword

    def setup(self, app):
        self.app = app

    def apply(self, callback, context):
        args = inspect.getargspec(context.callback)[0]

        if 'app' in args:

            def wrapper(*args, **kwargs):
                kwargs['app'] = self.app
                body = callback(*args, **kwargs)
                return body
            return wrapper

        return callback

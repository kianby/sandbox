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

        moreargs = {}
        if 'db' in args:
            moreargs['db'] = self.app.config['db']
        if 'auth' in args:
            moreargs['auth'] = self.app.config['factory'].getAuthService()
        if 'logger' in args:
            moreargs['logger'] = self.app.config['logger']

        if moreargs:
            def wrapper(*args, **kwargs):
                for k in moreargs:
                    kwargs[k] = moreargs[k]
                body = callback(*args, **kwargs)
                return body
            return wrapper
        else:
            return callback

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bottle import request, abort


class AuthPlugin(object):

    name = 'auth'
    api = 2

    def __init__(self, keyword='auth', **kwargs):
        self.keyword = keyword

    def setup(self, app):
        self.auth = app.config['factory'].getAuthService()

    def apply(self, callback, context):

        if not context.rule.startswith('/api'):
            return callback

        def wrapper(*args, **kwargs):
            username = request.get_header('User')
            token = request.get_header('Token')
            if self.auth.validate(username, token):
                body = callback(*args, **kwargs)
            else:
                body = abort(401, 'Unauthorized request')
            return body

        return wrapper

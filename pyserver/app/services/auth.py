#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar
import datetime
import jwt


class AuthService:

    def __init__(self, app):
        self.app = app
        self.db = app.config['db']
        self.secret = app.config['global.jwtsecret']
        self.delta = datetime.timedelta(seconds=600)

    def authenticate(self, username, password):
        BAD_RESULT = [None, None]
        try:
            user = self.db.users.find_one({'username': username})
            if user['username'] == username and user['password'] == password:
                d = datetime.datetime.utcnow() + self.delta
                exp = calendar.timegm(d.utctimetuple())
                token = jwt.encode({'user': username, 'exp': exp},
                                   self.secret,
                                   algorithm='HS256').decode()
                return [token, exp]
        except:
            # TODO log something
            pass
        return BAD_RESULT

    def validate(self, username, token):
        try:
            user = self.db.users.find_one({'username': username})
            decoded = jwt.decode(token, self.secret)
            print('Expiration : %d' % decoded['exp'])
            return user and user.get('username') == decoded['user']
        except:
            # TODO log something
            pass
        return False

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
        timeout = int(app.config['global.session_timeout'])
        self.idle_timeout = datetime.timedelta(minutes=timeout)

    def __authenticate(self, username, password):
        user = self.db.users.find_one({'username': username})
        return user and user['username'] == username and user['password'] == password

    def __cleanSessions(self):
        """Find and remove expired sessions"""
        when = datetime.datetime.utcnow() - self.idle_timeout
        self.db.sessions.remove({'used': {'$lt': when}})

    def login(self, username, password):
        try:
            if self.__authenticate(username, password):
                now = datetime.datetime.utcnow()
                at = calendar.timegm(now.utctimetuple())
                # encode 'at' to get a different token per user connection
                token = jwt.encode({'user': username, 'at': at},
                                   self.secret,
                                   algorithm='HS256').decode()
                self.db.sessions.insert({'username': username,
                                         'token': token,
                                         'login': now,
                                         'used': now})
                return token
        except:
            # TODO log something
            pass
        return None

    def validate(self, username, token):
        self.__cleanSessions()
        session = self.db.sessions.find_one({'username': username,
                                             'token': token})
        # update session last used
        if session:
            now = datetime.datetime.utcnow()
            self.db.sessions.update(session, {'$set': {'used': now}})
        return session

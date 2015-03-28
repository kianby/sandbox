#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar
import datetime
import jwt
import config
from app.models.user import User

import logging
logger = logging.getLogger(__name__)

def __authenticate(username, password):
    return User.get(User.username == username, User.password == password)

def __cleanSessions(self):
    """Find and remove expired sessions"""
    when = datetime.datetime.utcnow() - self.idle_timeout
    db.sessions.remove({'used': {'$lt': when}})

def login(username, password):
    try:
        if __authenticate(username, password):
            now = datetime.datetime.utcnow()
            at = calendar.timegm(now.utctimetuple())
            # encode 'at' to get a different token per user connection
            token = jwt.encode({'user': username, 'at': at},
                               self.secret,
                               algorithm='HS256').decode()
            # db.sessions.insert({'username': username,
            #                         'token': token,
            #                         'login': now,
            #                         'used': now})
            return token
    except:
        logger.exception('login failed')
    return None

def validate(username, token):
    self.__cleanSessions()
    session = self.db.sessions.find_one({'username': username,
                                         'token': token})
    # update session last used
    if session:
        now = datetime.datetime.utcnow()
        self.db.sessions.update(session, {'$set': {'used': now}})
    return session

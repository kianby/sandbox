#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app.services.auth import AuthService
from app.helpers.string_helper import StringHelper


class Factory:

    db = None
    auth = None

    def __init__(self, db=None):
        self.db = db

    def getAuthService(self):
        if self.auth is None:
            self.auth = AuthService()
        return self.auth

    def getStringHelper(self):
        return self._getService(StringHelper(self.db), [])

    def _getService(self, service, stuff):
        for item in stuff:
            service.inject(item[0], item[1])
        return service

    def _getDAO(self, dao):
        dao.inject("dateHelper", self.getDateHelper())
        return dao

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from core.services.auth import AuthService
from core.helpers.string_helper import StringHelper


class Factory:
    db = None

    def __init__(self, db):
        self.db = db

    def getAuthService(self):
        return self._getService(AuthService(self.db), [])

    def getStringHelper(self):
        return self._getService(StringHelper(self.db), [])

    def _getService(self, service, stuff):
        for item in stuff:
            service.inject(item[0], item[1])
        return service

    def _getDAO(self, dao):
        dao.inject("dateHelper", self.getDateHelper())
        return dao

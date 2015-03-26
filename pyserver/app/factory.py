#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app.services.auth import AuthService
from app.services.database import DatabaseService


class ServiceFactory:

    app = None
    auth = None
    db = None

    def __init__(self, app):
        self.app = app

    def getAuthService(self):
        if self.auth is None:
            self.auth = AuthService(self.app)
        return self.auth

    def getDatabaseService(self):
        if self.db is None:
            self.db = DatabaseService(self.app)
        return self.db

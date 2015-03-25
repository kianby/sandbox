#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app.services.auth import AuthService


class Factory:

    app = None
    auth = None

    def __init__(self, app):
        self.app = app

    def getAuthService(self):
        if self.auth is None:
            self.auth = AuthService(self.app)
        return self.auth

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from playhouse.db_url import connect

class DatabaseService:

    def __init__(self, app):
        self.app = app
        self.db = app.config['db']

    def setup():
        pass

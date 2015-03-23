#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Service:

    db = None

    def __init__(self, db):
        self.db = db

    def inject(self, key, value):
        self.__dict__[key] = value

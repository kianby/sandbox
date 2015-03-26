#!/usr/bin/python
# -*- coding: UTF-8 -*-

from peewee import Model
from peewee import CharField
from peewee import DateField
from server import db


class Session(Model):
    username = CharField()
    password = CharField()
    token = CharField()
    login = DateField()
    last_used = DateField()

    class Meta:
        database = db

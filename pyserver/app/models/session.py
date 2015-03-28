#!/usr/bin/python
# -*- coding: UTF-8 -*-

from peewee import Model
from peewee import CharField
from peewee import DateField
from app.services.database import get_db


class Session(Model):
    username = CharField()
    token = CharField()
    login = DateField()
    last_used = DateField()

    class Meta:
        database = get_db()

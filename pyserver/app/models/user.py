#!/usr/bin/python
# -*- coding: UTF-8 -*-

from peewee import Model
from peewee import CharField
from peewee import DateField
from app.services.database import get_db


class User(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = get_db()

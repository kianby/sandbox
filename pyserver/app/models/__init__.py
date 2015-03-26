#!/usr/bin/python
# -*- coding: UTF-8 -*-

from playhouse.db_url import connect

db = connect('sqlite:///default.db')

from app.models.session import Session

db.connect()
db.create_tables([Session])

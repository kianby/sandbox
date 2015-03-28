#!/usr/bin/python
# -*- coding: UTF-8 -*-

import functools
from config import DB_URL
from playhouse.db_url import connect


def get_db():
    return connect(DB_URL)

def provide_db(func):

    @functools.wraps(func)
    def new_function(*args, **kwargs):
        return func(get_db(), *args, **kwargs)

    return new_function

@provide_db
def setup(db):
    from app.models.session import Session
    from app.models.user import User
    db.create_tables([User, Session], safe=True)



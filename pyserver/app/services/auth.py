#!/usr/bin/python
# -*- coding: UTF-8 -*-


from app.service import Service


class AuthService(Service):

    def __init__(self):
        pass

    def login(self, login, password):
        return "Hello %s. Greetings to you!" % login

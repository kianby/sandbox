#!/usr/bin/python
# -*- coding: UTF-8 -*-


from core.service import Service


class AuthService(Service):

    def login(self, login, password):
        return "Hello %s. Greetings to you!" % login

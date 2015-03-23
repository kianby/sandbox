#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
from core.service import Service


class StringHelper(Service):

    def validEmail(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

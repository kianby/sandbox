#!/usr/bin/python
# -*- coding: UTF-8 -*-

import msgpack


class Message:

    def _data(self):
        pass

    def toWire(self):
        return msgpack.packb(self._data())


class Ping (Message):

    def _data(self):
        return {'m': 'ping'}

    def __repr__(self):
        return 'Ping'


class Pong (Message):

    def __init__(self, name):
        self.name = name

    def _data(self):
        return {'m': 'pong', 'n': self.name}

    def __repr__(self):
        return 'Pong from %s' % self.name


class InfoReq (Message):

    def __init__(self, name):
        self.name = name

    def _data(self):
        return {'m': 'inforeq', 'n': self.name}

    def __repr__(self):
        return 'InfoReq for %s' % self.name


class InfoResp (Message):

    def __init__(self, name, info):
        self.name = name
        self.info = info

    def _data(self):
        return {'m': 'inforesp', 'n': self.name, 'i': self.info}

    def __repr__(self):
        return 'InfoResp for %s: %s' % (self.name, self.info)


def decode(bytes):
    msg = msgpack.unpackb(bytes, encoding='utf-8')
    mobj = None
    if msg['m'] == 'ping':
        mobj = Ping()
    elif msg['m'] == 'pong':
        mobj = Pong(msg['n'])
    elif msg['m'] == 'inforeq':
        mobj = InfoReq(msg['n'])
    elif msg['m'] == 'inforesp':
        mobj = InfoResp(msg['n'], msg['i'])
    return mobj

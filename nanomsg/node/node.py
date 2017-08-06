#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import nnpy
import time
import json
from clize import clize, run
from microcore import message


@clize
def node(config_pathname, name):

    with open(config_pathname, 'rt') as config_file:
        config = json.loads(config_file.read())
    print(config)
    print('Node %s' % name)

    pub = nnpy.Socket(nnpy.AF_SP, nnpy.PUB)
    pub.connect(config['PubURL'])

    sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
    sub.connect(config['SubURL'])
    sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')

    time.sleep(1)

    while True:
        msg = message.decode(sub.recv())
        #print("msg: %s" % msg)
        if isinstance(msg, message.Ping):
            print('reply to Ping')
            resp = message.Pong(name)
            pub.send(resp.toWire())
        elif isinstance(msg, message.InfoReq) and msg.name == name:
            print('reply to InfoReq')
            info = {'status': True, 'endpoint':'http://127.0.0.1:8100'}
            resp = message.InfoResp(name, info)
            pub.send(resp.toWire())

if __name__ == '__main__':
    run(node)

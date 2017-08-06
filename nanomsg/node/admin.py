#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from clize import clize, run
import nnpy
import time
import json
from microcore import message


def die(error):
    print(error)
    sys.exit(1)


@clize
def admin(config_pathname, command, *arg):

    with open(config_pathname, 'rt') as config_file:
        config = json.loads(config_file.read())
    #print(config)

    pub = nnpy.Socket(nnpy.AF_SP, nnpy.PUB)
    pub.connect(config['PubURL'])

    sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
    sub.connect(config['SubURL'])
    sub.setsockopt(nnpy.SOL_SOCKET, nnpy.RCVTIMEO, 5000)
    sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')

    #time.sleep(1)

    reqmsg = None
    if command == 'ping':
        reqmsg = message.Ping()
    elif command == 'info':
        reqmsg = message.InfoReq(arg[0])

    if reqmsg is None:
        try:
            pub.close()
            sub.close()
        except:
            pass
        die('unsupported command: %s' % command)

    print('>> %s' % reqmsg)
    pub.send(reqmsg.toWire())

    received_data = False
    while True:
        try:
            msg = message.decode(sub.recv())
            if str(msg) != str(reqmsg):
                print('<< %s' % msg)
                received_data = True
        except nnpy.errors.NNError:
            if not received_data:
                print('No response')
            break
        except:
            print('Unexpected error: %s' % sys.exc_info()[0])
            break
    pub.close()
    sub.close()


if __name__ == '__main__':
    run(admin)

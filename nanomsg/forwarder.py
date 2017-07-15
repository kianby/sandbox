import nnpy
import time

pub = nnpy.Socket(nnpy.AF_SP, nnpy.PUB)
pub.bind('tcp://127.0.0.1:5555')

sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
sub.bind('tcp://127.0.0.1:5565')
sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')

while True:
    msg = sub.recv()
    print("forwarder log: %s" % msg)
    pub.send(msg)

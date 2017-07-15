import sys
import nnpy
import time

# nanocat --pub --connect-local 5565  --data "[A] status" -i 5

def node(name):

    print('Node %s' % name)

    pub = nnpy.Socket(nnpy.AF_SP, nnpy.PUB)
    pub.connect('tcp://127.0.0.1:5565')

    # bind node socket
    sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
    sub.connect('tcp://127.0.0.1:5555')
    sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')
    time.sleep(1)

    while True:
        msg = str(sub.recv(), 'utf-8')
        if msg.startswith('[%s]' % name):
            print("reply for msg: %s" % msg)
            pub.send("Ack from %s" % name)
        elif not msg.startswith('['):
            print("msg: %s" % msg)

if __name__ == '__main__':
    print(len(sys.argv), sys.argv)
    if len(sys.argv) > 1:
        node(sys.argv[1])

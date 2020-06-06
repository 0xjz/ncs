#!/usr/bin/env python
#-*- coding:utf-8 -*-
import readline
import socket
import ssl
import time
import threading
import sys



def recv_all(s):
    r = ''
    while True:
        ch = s.recv(1)
        if len(ch) == 0: break
        r += ch
    return r

def recv_print(s):
    while True:
        sys.stdout.write(s.recv(1))

class recv_thread(threading.Thread):
    def __init__(self, s):
        self.s = s
        threading.Thread.__init__(self)
    def run(self):
        while True:
            recv_print(self.s)
            # output = recv_all(self.s)
            # if output != '':
            #     print(output)
            #     time.sleep(1)


def work(domain_name, port):
    # conenction
    s = socket.create_connection((domain_name, port))
    s = ssl.wrap_socket(s)
    # receiver
    f = recv_thread(s)
    f.daemon = True
    f.start()
    # get input & send
    while True:
        request = ''
        while True:
            # line = sys.stdin.readline().rstrip('\n') + '\r\n'
            line = raw_input().rstrip('\n') + '\r\n'
            # print 'sending |' + line.encode('hex') + ' | ' + line
            s.send(line)



        #     request += line
        #     if request[:5] == 'POST ':
        #         if len(request) > 6 and request[-4:] == '\r\n\r\n' and request.count('\r\n\r\n') == 2:
        #             break
        #     elif request[:4] == 'GET ':
        #         if len(request) > 4 and request[-4:] == '\r\n\r\n':
        #             break
        # print 'sending:::\n' + request
        # s.sendall(request)




def main(argv):
    if len(argv) == 1:
        print('usage: %s domain ssl_port' % argv[0])
        return
    domain_name = argv[1]
    port = argv[2]
    work(domain_name, port)

if __name__ == '__main__':
    main(sys.argv)
    

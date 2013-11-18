#!/bin/env python2
#coding:utf-8

import struct
import socket
import select
import traceback
import threading
__DEBUG__ = True
class bad_data(Exception):
    pass

class socks5server:
    def __init__(self, ip='public_ip', port=5555):
        self.ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_ip = ip
        self.bind_port = port
        self.server_for_ever(ip, port)

    def server_for_ever(self, ip, port):
        self.ser_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ser_sock.bind((ip, port))
        self.ser_sock.listen(200)
        while True:
            cli, addrinfo = self.ser_sock.accept()
            if __DEBUG__:
                print "[*] get connect from %s:%s" % (addrinfo[0], addrinfo[1])
            p = threading.Thread(target=self.handler_cli, args=(cli,))
            p.start()
        # nerver reach here

    def handler_cli(self, cli_socket):
        dst_addr = dst_port = 0
        try:
            # handshake one
            data = cli_socket.recv(3)
            if data[0] != '\x05':
                raise bad_data
            if data[1] != '\x01' and data[2] != '\x00':
                if __DEBUG__:
                    print "[*] not support auth.. check client"
                raise bad_data
            req = '\x05\x00'; cli_socket.send(req)
            # handshake two
            data = cli_socket.recv(4)
            if data[0:3] != '\x05\x01\x00':
                raise bad_data
            #print "here?"
            if data[3] == '\x01':  # inet_ntoa ,ntohs
                data += cli_socket.recv(4 + 2)
                dst_addr = socket.inet_ntoa(data[4:-2])
                dst_port = int(socket.ntohs(data[-2:]))
            elif data[3] == '\x03':
                addr_len = ord(cli_socket.recv(1))
                data += cli_socket.recv(addr_len + 2)   # domain + port
                print "data : %s " % repr(data[4:-2])
                dst_addr = socket.gethostbyname(data[4:-2]) # 保证
                dst_port = int(struct.unpack('>H', data[-2:])[0])
            else:
                raise bad_data
        except bad_data:
            cli_socket.close()
            if __DEBUG__:
                print "bad_data %s" % repr(data)
            return False
        except:
            if __DEBUG__:
                print traceback.format_exc()
            return False
        if __DEBUG__:
            print " go foreign %s:%s" % (dst_addr, dst_port)
        dst_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        try:
            dst_socket.connect((dst_addr, dst_port))
            cli_socket.send('\x05\x00\x00\x01'+socket.inet_aton(self.bind_ip) \
                                    +struct.pack('>H', int(self.bind_port)))
        except:
            cli_socket.send('\x05\x05\x00\x01\x00\x00\x00\x00\x00\x00')  # 失败
            return
        print "success , start to trans data"
        self.trans_data(cli_socket, dst_socket)

    def trans_data(self, cli_socket, dst_socket):
        sock_list = (cli_socket, dst_socket)
        while True:
            (rlist, wlist, xlist) = select.select(sock_list, [], [])
            for i in rlist:
                if i == cli_socket:
                    data = i.recv(20)  # !! 会不会阻塞?
                    dst_socket.send(data)  # fixme!!
                elif i == dst_socket:
                    data = i.recv(20)
                    cli_socket.send(data)

# test
if __name__ == '__main__':
    c = socks5server(ip='192.168.253.129')

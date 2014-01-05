#coding:utf-8
import fcntl
import socket
import struct
ifname = b'eth0'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 0x8915 是 SIOCGIFADDR
ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
print(ip)

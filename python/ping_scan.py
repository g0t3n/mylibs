#!/bin/env python2
#coding:utf-8
import Queue
import platform
import re
import os
ips = []
ips.append("192.168.4.1")
ips.append("www.baidu.com")
pinglist = []
def pinger():
    global pinglist
    for ip in ips:
        if platform.system()=='Linux':
            p = os.popen('ping -c 2 ' + ip)
            m = re.search('(\d)\sreceived', p.read())
            try:
                if m.group(1)!='0':
                    pinglist.append(ip)
            except:
                pass
        if platform.system()=='Windows':
            p = os.popen('ping -n 2 ' + ip)
            m = re.search('TTL', p.read())
            if m:
                pinglist.append(ip)
            q.task_done()

if __name__== '__main__':
    pinger()
    print pinglist

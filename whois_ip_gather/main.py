#!/usr/bin/env python
# coding=utf-8
# Created Time: Sat Oct 18 15:30:14 2014
# Author: g0t3nst@gmail.com
import sys

from ipwhois import IPWhois

__DEBUG__ = True
queryed_ip_list = []

def get_ip_whois_info(ipaddr):
    '''
    Return Value
      whois_result_json: ip whois infomation with json format
      _ : ip hostname, look like gethostbyname(ip)
    '''
    try:
        obj = IPWhois(ipaddr)
    except IPDefinedError:
        if __DEBUG__:
            print "fine we get prive ip ;-)"
            return -1
    result = obj.lookup()
    dns_zone = obj.dns_zone
    return whois_result_json, osb.get_host()

def get_ips_from_stdin():
    if os.isatty( sys.stdin.fileno() ):
        ips = raw_input("IP addresses to query: ").split()
        print("")
    else:
        ips = sys.stdin.read().split()
    return ips

def get_some_ip_list(ip_dex_len):
    '''
    产生十进制 ip,随机 yield 几个值
    Return Value
    '''
    the_last = 255*256*256*256 + 255*256*256 + 255*256 + 256 #4294967296
    for ip_dex in xrange(the_last):
        ip_d = ip_dex % 256
        ip_c = (ip_dex - ip_d) / 256
        ip_b = (ip_dex - ip_d - ip_c*256) / 256
        ip_a = (ip_dex - ip_d - ip_c*256 - ip_b*256*256) / 256
        ip_ascii = "%s.%s.%s.%s" % (ip_a, ip_b, ip_c, ip_d)
        yield ip
def main():
    for 


if __name__ == '__main__':
    main()

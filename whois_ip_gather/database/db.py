#!/usr/bin/env python
# coding=utf-8
# Created Time: Wed Oct 22 15:06:39 2014
# Author: g0t3nst@gmail.com

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

BaseDb = declarative_base()
__MYSQL_USER__ = ''
__MYSQL_PASS__ = ''



def init_db():
    for i in range(255):
        t = Table('WhoisIp%s' % str(i), metadata,
                Column('id', Integer, primary_key=True),
                Column('ipfrom', Integer, unique=True, nullable=False),
                Column('ipto', Integer, unique=True, nullable=False),
                Column('whoisData', String, collation='utf8', unique=True,
                    nullable=False)
                )
        # 找到 Table 中最大的
# SELECT MAX(ipto) FROM WhoisIpPrefix;
def self_test_main():
    engine = create_engine("mysql://%s:%s@localhost/test" % \
            (__MYSQL_USER__, __MYSQL_PASS__),
            isolation_level="READ UNCOMMITTED"
            )
    init_db()
    return


if __name__ == '__MAIN__':
    self_test_main()

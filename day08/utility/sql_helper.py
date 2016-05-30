#!/usr/bin/env python
# coding:utf-8


'''
Created on 2016��5��27��

@author: lenovo
'''
import MySQLdb

#yin ru pei zhi wen jian(conf)

import conf
class MySqlHelper(object):
    
    def __init__(self):
    
        self.__conn_dict = conf.conf
#         self.__conn_dict = dict(host='192.168.0.143', user='root', passwd='whjx*8888', db='test')
    # ��ȡȫ������
    def Get_Dict(self, sql, params):
#         con = MySQLdb.connect(host='192.168.0.143', user='root', passwd='whjx*8888', db='test')
        con = MySQLdb.connect(**self.__conn_dict)
        cur = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        con.close()
        return data
    
    def Get_One(self, sql, params):
#         con = MySQLdb.connect(host='192.168.0.143', user='root', passwd='whjx*8888', db='test')
        con = MySQLdb.connect(**self.__conn_dict)
        cur = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        con.close()
        return data

if __name__ == '__main__':
    helper = MySqlHelper()
    sql = "select * from salor where id>%s"
    params = (1,)
    dict_data = helper.Get_Dict(sql, params)
    print dict_data
    dict_one = helper.Get_One(sql, params)
    print dict_one
        
    

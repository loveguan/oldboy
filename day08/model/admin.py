#!/usr/bin/env python
#coding:utf-8

from utility.sql_helper import MySqlHelper
class Admin(object):
    
    def __init__(self):
        self.__helper = MySqlHelper()
        
        
    def Get_One(self,id):
        sql = "select * from salor where id=%s"
        params = (id,)
        return self.__helper.Get_One(sql, params)
    
    def CheckValidate(self,username,password):
        try:
            sql = "select address from salor where name=%s and address=%s"
            params = (username,password)
            test=self.__helper.Get_One(sql, params)
            print test
            return test
        except Exception,e:
            return None 
    

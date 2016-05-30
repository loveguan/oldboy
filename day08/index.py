#!/usr/bin/env python
#coding:utf-8

from model.admin import Admin

def main():
    user = raw_input('username: ')
    pwd = raw_input('passwd: ')
    admin = Admin()
    result=admin.CheckValidate(user, pwd)
    if result:
        print 'ok'
    else:
        print 'wrong password!'
    
if __name__=='__main__':
    main()
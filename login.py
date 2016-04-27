#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys
import os

retry_limit = 3 #最多重试的次数
retry_count = 0 #计数

account_file = 'accounts.txt' #用户名和密码存放文件
lock_file = 'lock.txt' #存放锁定用户文件

while retry_count < retry_limit:
    username = raw_input('\033[32;1m input username:\033[0m') #输入用户名
    lock_check = file(lock_file)
    for line in lock_check.readlines():
        name = line.strip('\n').split()[0]
        if username == name:
            sys.exit('\033[31;1mUser %s is locked!\033[0m' %username)  #如果在锁定文件里，直接退出

    passwd = raw_input('\033[32;1m input passwd:\033[0m') #输入密码
    f = file(account_file)
    match_flag = False
    for line in f.readlines():
        user,pwd = line.strip('\n').split()
        if username == user and passwd == pwd:  #根据帐号密码判断是否匹配
            print 'match!', username
            match_flag = True     #设置标志位
            break

    f.close()

    #根据判断输出信息或者重新再来在允许的次数范围内

    if match_flag == False:
        print 'wrong passwd'
        retry_count +=1
    else:
        print 'welcome,',username #成功登录，显示欢迎信息

else:
    print 'your count is locked'
    f = file(lock_file,'ab')
    f.write(username+os.linesep )  #添加换行符
    f.close()




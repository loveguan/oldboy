#!/usr/bin/env python
#_*_ coding:utf-8 _*_


f = file('xingming.txt','r')

string = raw_input("please input your sting:")
y = 0

for i in f.xreadlines():
    # print i.strip()
    if string in i:
        y = y+1
        print i.strip().replace(string,'\033[32;1m %s\033[0m' %string)

print 'find %d items contain %s' %(y,string)
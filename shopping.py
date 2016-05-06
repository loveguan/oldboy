#!/usr/bin/env python
#_*_ coding:utf-8 _*_

total_price = 20000 # 拥有的金额
list = []

while total_price > 0: #while loop
    print '''===== shoping list =====
item apple, price 10
item orange, price 20
item iphone,price 5000
item python,price 10000
======================
'''
    i = raw_input('please input your choice:')  # please input you choice
    if i == 'apple':
        price = 10
    elif i == 'orange':
        price = 20
    elif i == 'iphone':
        price = 5000
    elif i == 'python':
        price =  10000

    if total_price-price < 0: #看循环条件是否成立
        print 'you have only %s' %total_price
        continue

    list.append(i)
    total_price -=price
    print total_price

    message = raw_input('do you want to continue,y or n :')
    while message not in "y,n":
        message = raw_input('do you want to continue,y or n:')
    if message == 'n':
        break
print list
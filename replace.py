#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys,os

if len(sys.argv) < 4: #limit the arguements lager 4
    print "usage: ./file_replace.py old text new_text filename"
old_text,new_text = sys.argv[1],sys.argv[2] #get the old and new item
file_name = sys.argv[3] #get the file name
f = file(file_name,'rb')
new_file = file('.%s.bak' %file_name,'wb')
for i in f.xreadlines(): #for intera  to replace
    print i.replace(old_text,new_text)
    new_file.write(i.replace(old_text,new_text))

f.close()
new_file.close()

if '--back' in sys.argv: #if --back exits, replace the old one with the new
    os.rename(file_name,'.%s.bak2' %file_name)
    os.rename('.%s.bak'% file_name,file_name)



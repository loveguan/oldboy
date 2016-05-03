
a= [1,2,2,3,4,5,5,5,5,3,2,1,2,4,6,4,6,3,2,9,8,6,5,4,3,2]

pos = 0
for i in range(a.count(2)):
    if pos == 0:
       pos = a.index(2,pos)
    else:
       pos = a.index(2,pos+1)
    print pos
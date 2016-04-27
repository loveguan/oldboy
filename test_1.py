f = file('myFile.txt','r')
for line in f.readlines():
    line = line.strip().split(':')
    print line
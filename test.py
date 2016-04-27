this_year = 2016
name = raw_input('please input your name:')
age =int( raw_input(('please input your age:')))
sex = raw_input("please input your sex:")
dep = raw_input("which department:")
message = '''Infornation of the company staff:
        Name: %s
        Age : %d
        Sex : %s
        Dep : %s
''' %(name,age,sex,dep)
print message
print "Hello,", name,'\n'
print "you are", age, 'years'
print "so you were born in: ", this_year - age

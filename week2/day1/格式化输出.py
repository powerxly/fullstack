# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2018/11/23

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():#长得像不像数字，比如200d，'200'
    salary = int(salary)
# else:
#      exit("must input digit")
# # print(name,age,job,salary)

msg = '''
---------- info of %s --------
Name:%s
Age :%s
Job :%s
Salary:%f
You will be retired in %s years
-------- END --------
''' % (name,name,age,job,salary,65-age)
print(msg)
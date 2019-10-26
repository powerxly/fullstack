# -*- coding: utf-8 -*-
#__author:jason
#date:2019/8/6

class Employee:
    "所有员工的基类"
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d"%Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)
#创建Employee类的第一个对象
emp1 = Employee("zara",2000)
#创建Employee类的第一个对象
emp2 = Employee("Manni",5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

emp1.age = 7
emp1.age = 8
hasattr(emp1,"age")
setattr(emp1,'bigname',"hahaha")
emp1.displayEmployee()
print(emp1.bigname)



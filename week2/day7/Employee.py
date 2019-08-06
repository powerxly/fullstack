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

emp1 = Employee("zara",2000)
emp2 = Employee("Manni",5000)

emp1.emp2.displayCount()


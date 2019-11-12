# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 10:43 下午
# @Author  : jasonleeyag@gmail.com
# @FileName: 11.5.1-jicheng.py
# @Software: PyCharm
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        template = 'Person [name{0},age{1}]'
        s = template.format(self.name,self.age)
        return s

class Student(Person):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        self.school = school




# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 10:50 下午
# @Author  : jasonleeyag@gmail.com
# @FileName: 11.5.2-chongxie.py
# @Software: PyCharm
class Animal(object):
    def __init__(self,age,sex=1,weight = 10):
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        self.weight +=0.01
        print('动物吃')

class Dog(Animal):
    def eat(self):
        self.weight +=0.05
        print("狗吃")
        print(self.weight)

a1 = Dog(2,0,10)
a1.eat()
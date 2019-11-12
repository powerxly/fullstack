# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 8:45 下午
# @Author  : jasonleeyag@gmail.com
# @FileName: Animal.py
# @Software: PyCharm
class Animal(object):
    def __init__(self,age,sex=1,weight=0.0):
        self.age = age
        self.sex = sex
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,weight):
        self.__weight = weight

a1 = Animal(2,0,10.0)
a1.weight = 123.45
print("a1体重：{0:.2f}".format(a1.weight))
#
# class Account:
#     """定义银行账户类"""
#
#     interest_rate = 0.0668  #类变量利率
#
#     def __init__(self,owner,amount):
#         self.owner = owner
#         self.amount = amount
#
# account = Account('Tony',1_800_000.0)
#
# print('账户名{0}'.format(account.owner))
# print('账户金额{0}'.format(account.amount))
# print('利率{0}'.format(Account.interest_rate))
# class Account:
#     """定义银行账户类"""
#
#     interest_rate = 0.0668
#
#     def __init__(self,owner,amount):
#         self.owner = owner
#         self.amount = amount
#
#     #类方法
#     @classmethod
#     def interest_by(cls,amt):
#         return cls.interest_rate * amt
#
#     #静态方法
#     @staticmethod
#     def interest_with(amt):
#         return Account.interest_by(amt)
#
# interest1 = Account.interest_by(12_000.0)
# print('计算利息:{0:.4f}'.format(interest1))
# interest2 = Account.interest_with(12_000.0)
# print('计算利息:{0:.4f}'.format(interest2))


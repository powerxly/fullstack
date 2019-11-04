# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 9:43 下午
# @Author  : jasonleeyag@gmail.com
# @FileName: shengchengqi.py
# @Software: PyCharm
from functools import reduce
a = (1,2,3,4,5)
a_reduce =reduce(lambda acc,i : acc + i , a,3)
print(a_reduce)
# def square(num):
#     for i in range(1, num + 1):
#         yield i*i
#
# for i in square(5):
#     print(i, end=" ")
# def calculate_fun(opr):
#     if opr == '+':
#         return lambda a,b:(a+b)
#     else:
#         return lambda a,b:(a-b)
# f1 = calculate_fun('+')
# f2 = calculate_fun('-')
#
# print(type(f1))
#
# print("10 + 5 = {0}".format(f1(10,5)))
# print("10 - 5 = {0}".format(f2(10,5)))
# user = ['Tony','Tom',"Ben","Alex"]
#
# # user_filter = filter(lambda u : u.startswith("T"),user)
# # print(list(user_filter))
# number_list = range(1,11)
# number_filter = filter(lambda it : it % 2 == 0,number_list)
# print(list(number_filter))
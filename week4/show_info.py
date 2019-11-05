# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 16:16
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com
#

from functools import reduce
# def show_info(sep=':',**info):
#     print('-----info-----')
#     for key,value in info.items():
#         print('{0}{2}{1}'.format(key,value,sep))
#     return


# result = show_info('->',name="tony",age=18,sex=True)
# print(result)
# show_info(sutdent_name='Tony',sutdent_no='1000',sep='-')
# stu_dict = {'name':'Tony','age':18}
# show_info(**stu_dict,sex=True,sep='=')

# def position(dt,speed):
#     posx = speed[0] * dt
#     posy = speed[1] * dt
#     return (posx,posy)
#
# move = position(60.0,(10,-5))
# print("物体位移：（{0},{1}）".format(move[0],move[1]))

a = (1,2,3,4,5)
a_reduce = reduce(lambda acc,i:acc+i,a)
print(a_reduce)
# -*- coding: utf-8 -*-
#__author:jason
#date:2019/7/29

dic1 = {'name':'alex'}
dic1['age']=18
print(dic1)



ret=dic1.setdefault('hobby','girl')
dic1.setdefault('hobby','girl')
print(ret)
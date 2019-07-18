# -*- coding: utf-8 -*-
#__author:jason
#date:2019/7/18

# name = 'wuchao'
# name1 = 'jinxin'
# name2 = 'xiaohu'
# name3 = 'sanpang'
# name4 = 'ligang'
#
# names = 'wuchao jinxin xiaohu sanpang ligang'

#字典的增删改查

#增  切片

# print(a[1:])#取值到最后
# print(a[1:-1])#取到倒数第二值
# print(a[1:-1:1])#从左到右步长为1 一个一个去取值
# print(a[1::2])#从左到右步长为2去取值
# print(a[3::-1])#从右到左步长为2去取值
# b = a[3::-1]
# print(b)
# print(a)

#添加
# a.append("xuepeng") #默认插入到最后一个位置
# print(a)
# a.insert(1,"xuepeng") #默认插入到任意一个位置
# print(a)

#修改

# a[1] = "ali"
# print(a)
# a[1:3] = ["a","b"]
# print(a)


#删除 remove pop del
# a.remove(a[0:3])
# print(a)
# b = a.pop(1)
# print(a)
# print(b)
# del a[0]
# print(a)
# del a
# print(a)

# count：计算某元素出现次数

# t = ["to","be","or","not","to","be"].count("to")
# print(t)


# extend 扩展

# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)
# print(b)

# index 根据内容找位置
# a = ["wuchao","jinxin","ligang","xiaohu","sanpang","wanghuan","ligang"]
#
# first_lg_index = a.index("ligang")
#
# little_list = a[first_lg_index+1:]
#
# second_lg_index = little_list.index("ligang")
# print(first_lg_index)
# print(second_lg_index)
# print(first_lg_index+second_lg_index)

# reverse 颠倒列表中的值

# a = ["wuchao","jinxin","ligang","xiaohu","sanpang","wanghuan","ligang"]
#
# a.reverse()
#
# print(a)

#  sort 对列表进行排序
x = [4,6,2,1,7,9]
x.sort(reverse=True)
print(x)

a = ["wuchao","jinxin","Ligang","Xiaohu","sanpang","wanghuan","ligang"]
a.sort()

print("liyang" in a)

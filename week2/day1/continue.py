# -*- coding: utf-8 -*-
#__author:jason
#date:2019/7/18
exit_flag = False

for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("layer2",j)
        if j==6:
            exit_flag = True
            break
    if exit_flag:
        break
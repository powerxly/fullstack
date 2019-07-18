# -*- coding: utf-8 -*-
#__author:jason
#date:2019/7/18

_user = "jason"
_passwd = "abc123"

counter = 0

while counter < 3 :
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("Welcome %s login...." % _user)
        break  # 跳出，中断

    else:
        print("invalid username or password!")
    counter += 1
    if counter == 3:
        keep_going_choice = input("还来么？[y/n]")
        if keep_going_choice == "y":
            counter = 0
else:
    print("不要脸！！！不要脸！！！")

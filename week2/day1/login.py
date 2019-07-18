# -*- coding: utf-8 -*-
#__author:jason
#date:2019/7/18

# for i in range(1,101):
#     if i % 2 == 1:
# #         print(i)
# for i in range(1,101,2):
#         print(i)
#
# for i in range(100):
#     if i<50 or i>70:
#         print(i)


_user = "jason"
_passwd = "abc123"
#passed_authentication = False

for i in range(3):

    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("Welcome %s login...." %_user)
        #passed_authentication = True
        break #跳出，中断

    else:
        print("invalid username or password!")
#if not passed_authentication:
else:
    print("3 times out")
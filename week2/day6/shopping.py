# -*- coding: utf-8 -*-
#__author:jason
#date:2019/7/18


product_list=[
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),

]
salary=input('please input your money:')
shopping_car=[]
if salary.isdigit():
    salary=int(salary)
    while True:
        #打印商品内容
        for i,v in enumerate(product_list,1):
            print(i,'>>>>',v)

         #引导用户选择商品
        choice=input('选择购买商品编号[退出：q]：')

        #验证输入是否合法
        if choice.isdigit():
            choice=int(choice)
            if choice>0 and choice<=len(product_list):
                #将用户选择商品通过choice取出来
                p_item=product_list[choice-1]

                #如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                if p_item[1] < salary:
                    salary-=p_item[1]

                    shopping_car.append(p_item)

                else:
                    print('余额不足，还剩%s'%salary)
                print(p_item)
            else:
                print('编码不存在')
        elif choice=='q':
            print('------------您已经购买如下商品----------------')
            #循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱'%salary)
            break
        else:
            print('invalid input')


# 购物车程序
#         salary = 5000
#         1.  iphone6s  5800
#         2.  mac book    9000
#         3.  coffee      32
#         4.  python book    80
#         5.  bicycle         1500
#       >>>:1
#          余额不足，-3000
#       >>>:5
#       已加入bicyle 到你的购物车， 当前余额:3500
#       >>>:quit
#       您已购买一下商品
#       bicyle    1500
#       coffee    30
#       您的余额为:2970
#       欢迎下次光临
#
#        balance 余额
#       salary 工资
#       购物车列表 shopping trolley
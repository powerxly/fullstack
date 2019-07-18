# -*- coding:utf-8 -*-

menu = {
    "北京":{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                'CCTV':{}
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{}
            },
            '三里屯':{
                '优衣库':{},
                '苹果':{}
            }

        },
        '西城':{},
        '东城':{},
    },
    "上海":{},
    "山东":{},
}
back_flag = False
exit_flag = False
while not back_flag and not exit_flag:
    for key in menu:
        print(key)
    choice = input(">>:").strip()
    if choice in menu:
        while not back_flag and not exit_flag:
            for key2 in menu[choice]:
                print(key2)
            choice2 = input(">>:").strip()
            if choice2 == 'b':
                back_flag = True
            if choice2 == 'q':
                exit_flag = True
            if choice2 in menu[choice]:
                while not back_flag and not exit_flag:
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    choice3 = input('>>:').strip()
                    if choice3 == 'b':
                        back_flag = True
                    if choice3 == 'q':
                        exit_flag = True
                    if choice3 in menu[choice][choice2]:
                        while not back_flag and not exit_flag:
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            choice4 = input('>>:').strip()
                            if choice4 == 'b':
                                back_flag = True
                            if choice4 == 'q':
                                exit_flag = True
                        else:
                            back_flag = False
                else:
                    back_flag = False
        else:
            back_flag = False


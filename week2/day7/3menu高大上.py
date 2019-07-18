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

current_layer = menu #实现动态循环
# parent_layer = menu

parent_layers = [] #保存所有父级，最后一个元素永远都是父级
while True:
    for key in current_layer:
        print(key)
    choice = input('>>:').strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        #进入下一层之前，把当前层追加到列表中，下一次loop，当用户选择b的时候，可以直接取列表的最后一个值出来
        current_layer = current_layer[choice]#改成了子层
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()#取出列表的最后一个值，因为当前
    else:
        print('无此项')
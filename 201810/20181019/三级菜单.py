#__author:"Peter"
#date:2018/10/19

menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                '渣打银行':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                'APPLE':{},
            }
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '阿泰包子':{},
            },
            '天通苑':{
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{},
        },
        '海淀':{
            '五渡口':{
                '谷歌':{},
                '网易':{},
                'sohu':{},
                'sogo':{},
                '快手':{},
            },
            '中关村':{
                'sohu':{},
                'Iqiyi':{},
                '汽车之家':{},
                '新东方':{},
                'QQ':{},

            },
        },
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'sohu':{},
                '高盛':{},
                '摩根':{},
            },
            '外滩':{},
        },
        '闵行':{},
        '静安':{},

    },
    '山东':{
        '济南':{
        },
        '青岛':{},
        '德州':{
            '乐陵':{
                '丁务镇':{},
                '城区':{},
            },
            '平原':{},

        },

    },
}

# while True:
#     for key in menu:
#         print(key)
#     choice = input('1>>:').strip()
#     if choice in menu:
#         while True:
#             for key2 in menu[choice]:
#                 print(key2)
#             choice2 = input("2>>:").strip()
#             if choice2 in menu[choice]:
#                 while True:
#                     for key3 in menu[choice][choice2]:
#                          print(key3)
#                     choice3 = input('3>>:').strip()
#
exit_flag = False
current_layer = menu

layers = [menu]

while not  exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #print("change to laster", current_layer)
        layers.pop()
    elif choice not  in current_layer:continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]

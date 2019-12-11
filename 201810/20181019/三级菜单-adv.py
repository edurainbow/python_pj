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
            },
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

current_layer = menu
#parent_layer = menu
parent_layers =[]
while True:
    for key in current_layer:
        print(key)
    choice = input('>>>:').strip()
    if  len(choice) == 0:continue
    if choice in current_layer:
        #parent_layer = current_layer
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
         #current_layer = parent_layer
         if parent_layers:
            current_layer = parent_layers.pop()
    else:
        print("无此项")




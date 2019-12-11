#__author:"Peter"
#date:2018/10/15

product_list=[
    ('mac',9000),
    ('kindle', 800),
    ('tesla', 900000),
    ('python book', 105),
    ('bike', 2000),
]
saving=input('please input your saving:')
shopping_car = []
if  saving.isdigit():
    saving=int(saving)
    # for i in product_list:
    #     print(1+product_list.index(i),i)
    while True:

        for i,v in enumerate(product_list,1):
            print(i,v)

        choice = input('选择购买商品编号[退出：q]：')
        if choice.isdigit():
            choice=int(choice)
            if choice > 0 and choice <= len(product_list):
                p_item = product_list[choice-1]
                if p_item[1] < saving:
                    saving-=p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，还剩%s元'%saving)
                print(p_item)
            else:
                print('编号不存在')
        elif choice == 'q':
            print('------您已经购买以下商品------------')
            for i in shopping_car:
                print(i)
            print('您还剩%s元'%saving)
            break
        else:
            print('invalid input')


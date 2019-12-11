#__author:"Peter"
#date:2018/10/30
# def show_shopping_car():
#     saving = 1000000
#     shopping_car = [
#         ('Mac', 9000),
#         ('kindle', 800),
#         ('tesla', 100000),
#         ('Python book', 105),
#     ]
#     print('您已经购买的商品如下'.center(50, '*'))
#     for i, v in enumerate(shopping_car, 1):
#         print('\033[35;1m %s:  %s \033[0m' % (i, v))
#
#     expense = 0
#     for i in shopping_car:
#         expense += i[1]
#     print('\n\033[32;1m您的余额为 %s \033[0m' % (saving - expense))
# show_shopping_car()
# def logger(log_test):
#     f = open("log.txt", 'a')
#     f.write("2018-11-02 0:51 %s" % log_text )
#     f.close()
#     print("2018-11-02 0:51 exec function 1")
#
# print("---function 1")
# logger("2018-11-02 0:51 exec function 1")
#
# print("---function 2")
# logger("2018-11-02 0:51 exec function 2")

# def f():
#     print('ok')
# f()

# def add(x,y):
#     print(x+y)
# add(10,20)

# def f(index):
#     print('function %s' % index)
# f(3)
# f(5)
import time
def logger(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)

    with open('日志记录','a') as f:
        f.write('%s end action%s\n'%(time_current,n))
def action1(n):
    print ('starting action1...')
    logger(n)

def action2(n):
    print ('starting action2...')
    logger(n)

def action3(n):
    print ('starting action3...')
    logger(n)

action1(11)
action2(22)
action3(33)


##***************代码重用

# def logger(n):
#     with open('日志记录','a') as f:
#         f.write('end action%s\n'%n)
#
# def action1():
#     print ('starting action1...')
#     logger(1)
#
#
# def action2():
#     print ('starting action2...')
#     logger(2)
#
#
# def action3():
#     print ('starting action3...')
#     logger(3)
#
#
# action1()
# action2()
# action3()
#
# ##***************可扩展和保持一致
# ##为日志加上时间
# import time
#
# def logger(n):
#     time_format='%Y-%m-%d %X'
#     time_current=time.strftime(time_format)
#
#     with open('日志记录','a') as f:
#         f.write('%s end action%s\n'%(time_current,n))
#
# def action1():
#     print ('starting action1...')
#     logger(1)
#
#
# def action2():
#     print ('starting action2...')
#     logger(2)
#
#
# def action3():
#     print ('starting action3...')
#     logger(3)
#
# action1()
# action2()
# action3()
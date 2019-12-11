#__author:"Peter"
#date:2018/11/7


# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner
#outer()()
# f = outer()
# f()

import time
# start = time.time()
# time.sleep(1)
# end=time.time()
# print(end-start)
# print(start)

# def show_time(f):
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print('spend %ss' % (end - start))
#     return inner
#
# @show_time # foo=show_time(foo)
# def foo():
#     print('foo....')
#     time.sleep(2)
#
#
# @show_time #bar=show_time(bar)
# def bar():
#     print('bar....')
#     time.sleep(3)
#
# foo()
# bar()




# def show_time(f):
#     def inner(*x,**y):
#         start=time.time()
#         f(*x,**y)
#         end=time.time()
#         print('spend %s'%(end-start))
#     return inner
# @show_time
# def add(*a,**b):
#     sums=0
#     for i in a:
#         sums+=i
#     print(sums )
#     time.sleep(1)
# add(1,2,5,7,9,5)

def logger(flag=''):
    def show_time(f):
        def inner(*x, **y):
            start = time.time()
            f(*x, **y)
            end = time.time()
            print('spend %s' % (end - start))
            if flag == 'true':
                print('日志记录')
        return inner
    return show_time

@logger('true')
def add(*a,**b):
    sums=0
    for i in a:
        sums+=i
    print(sums )
    time.sleep(1)
add(1,2,5,7,9,5)

@logger()
def bar():
    print('bar....')
    time.sleep(3)

bar()
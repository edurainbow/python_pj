#__author:"Peter"
#date:2018/11/9


# s=(x*2 for x in range(10000000000000))
# print(s)

# print(next(s))
# print(next(s))

# for i in s:
#     print(i)

# def foo():
#     print('ok')
#     yield 1
#     print('ok2')
#     yield 2
# g=foo()
# next(g)
# next(g)

# for i in g:
#     print(i)

# def fib(max):
#     n, b, a = 0, 0, 1
#     while n < max:
#         #print(a)
#         yield b
#         b, a = a, b + a
#         n = n + 1
#     return 'done'
# g=fib(8)
#
# print(next(g))

# def bar():
#     print('ok1')
#     count=yield 1
#     print(count)
#
#     yield 2
# b=bar()
# b.send(None)
# ret=b.send('eee')
# print(ret)


import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
        baozi = yield

        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i+1)

producer("alex")
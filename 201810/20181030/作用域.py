#__author:"Peter"
#date:2018/11/3

# if True:
#     x=3
# print(x)

# def f():
#     a=10
# print(a)

# x = int(2.9)  # int built-in
#
# g_count = 0  # global
# def outer():
#     o_count = 1  # enclosing
#     def inner():
#         i_count = 2  # local
#         print(o_count)
#     # print(i_count) 找不到
#     inner()
# outer()

# count = 10
#
# def outer():
#     global count
#     print(count)
#     count = 5
#     print(count)

# s2=set('alviin')
# #s2.update('op')
# s2.add('op')
# print(s2)

# def foo3():
#     def inner():
#         return 8
#     return inner
# ret=foo3()
# print(ret())

# def f(n):
#     return n*n
# def foo(a,b,func):
#     ret=func(a)+func(b)
#     return ret
# print(foo(2,4,f))
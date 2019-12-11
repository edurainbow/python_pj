#__author:"Peter"
#date:2018/11/4

# def fat(n):
#     ret=1
#     for i in range(1,n+1):
#         ret*=i
#     return ret
# print(fat(5))



# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))
#0 1 1 2 3 5 8 13 21 34 55

# def fibo(n):
#     # before=0
#     # after=1
#     # if n <= 2:
#     #     return n
#     if n==0 or n==1:
#         return n
#
#     return fibo(n-1)+fibo(n-2)
# print(fibo(10))

from functools import reduce
print (reduce(lambda x,y: x*y, range(1,6)))



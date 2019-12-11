#__author:"Peter"
#date:2018/11/3

# def f():
#     print('ok')
#     return

def add(*args):
    #print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)
    return sum
a=add(1,4)
print(a)

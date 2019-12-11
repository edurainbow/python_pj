#__author:"Peter"
#date:2018/11/2

# def print_info(name,age):
#     print('Name: %s'%name)
#     print('Age: %s'%age)
# print_info('Xiaohu',39)

# def print_info(name,age,sex='male'):
#     print('Name: %s'%name)
#     print('Age: %d'%age)
#     print('Sex: %s' %sex)
# print_info('Xiaohu',39)

# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
#
# add(4,5,6)

def print_info(sex='male',*args,**kwargs):
    print(args)
    #print(kwargs)
    for i in kwargs:
        print('%s:%s'%(i,kwargs[i]))

print_info('female','Xiaohu',39,job='IT',hobby='girls',height=188)
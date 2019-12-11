#__author:"Peter"
#date:2018/10/17
#创建字符串
var1 =  'Hello World!'
var2 = 'Python RAlvin'

#对应操作：
#print('hello'*2) #重复输出字符串
# print('helloworld'[2:])
#print('el' in 'hello')
#print('alex is a good teacher')
# print('%s is a good %s' %('alex','teacher'))
# a='123'
# b='abc'
# c='789'
# # d1=a+b+c
# # print(d1)
# d2 =''.join([a,b,c])
# print(d2)

#python的内置方法
st='hello kitty  {name} is {age}'
# print(st.count('l'))
# print(st.capitalize())
# print(st.center(50,'-'))
# print(st.endswith('y'))
# print(st.startswith('he'))
#print(st.expandtabs(tabsize=10))
# print(st.find('k'))
# print(st.format(name='alex',age=38))
print(st.format_map({'name':'alex','age':38}))
# print(st.index('t'))
# print(st.isalnum())
# print('1'.isdigit())
# print('ab'.isidentifier())
# print('abc'.islower())
# print('ABC'.isupper())
# print(' '.isspace())
# print('Abc'.istitle())
# print('My Title'.lower())
# print('My Title'.upper())
# print('My Title'.swapcase())
# print('My Title'.ljust(50,'*'))
# print('My Title'.rjust(50,'*'))
# print('  My Title \n'.strip())
# print('My Title'.replace('itle','lesson'))
# print('My Title'.split('i'))
# print('My title'.title())

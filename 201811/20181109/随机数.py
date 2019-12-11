#__author:"Peter"
#date:2018/11/23

import random
# print(random.random())
# print(random.randint(1,8))
#print(random.choice('hello'))
#print(random.choice(('123',4,(1,2))))
#print(random.sample(('123',4,(1,2)),2))
#print(random.randrange(1,3))


def v_code():
    code=''
    for i in range(5):
        add=random.choice((random.randrange(10),chr(random.randrange(65,91))))
        code+=str(add)

    print(code)
v_code()


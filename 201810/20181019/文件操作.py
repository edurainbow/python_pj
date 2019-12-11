#__author:"Peter"
#date:2018/10/20

#data=open('小重山','r',encoding='utf8').read()
# f=open('小重山','r',encoding='utf8')
# data=f.read()
#f.write('\nhello world \n')
#f.write('alex')
# print(data)
#a=f.readline()
# print(f.readline())
# print(f.readline())
#print(f.readlines())
# for i in f.readlines():
#     print(i.strip())

# number = 0
# for i in f.readlines():
#     number+=1
#     if number==6:
#         #print(i.strip(),'ikeit')
#         #i=i.strip()+'ikeit'
#         i=''.join([i.strip(),'111'])
#     print(i.strip())

# print(f.tell())
# print(f.read(4))
# print(f.tell())
# f.seek(0)
# print(f.read(4))
# f.close()

# import sys,time
# for i in range(30):
#     # sys.stdout.write("*")
#     # sys.stdout.flush()
#     print('*',end='',flush=True)
#     time.sleep(0.1)
# f=open('小重山','a',encoding='utf8')
# f.truncate(5)
# print(f.isatty())

# f_read=open('小重山','r',encoding='utf8')
# f_write=open('小重山','w',encoding='utf8')
# number=0
# for line in f_read:
#     number+=1
#     if number==5:
#         line=''.join([line.strip(),'alex\n'])
#     f_write.write(line)

# f=open('log','r')
# f.readline()
# f.read()
# f.close()
#
# with open('log','r') as f:
#     f.readline()
#     f.read()
# print('hello')

with open('log1','r') as f_read,open('log2','w') as f.write:
    for line in f_read:
        f_write.write(line)

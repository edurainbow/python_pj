#__author:"Peter"
#date:2018/11/23

import time
#print(help(time))
#print(time.time())#时间戳
#time.sleep(3)
#print(time.clock()) #计算CPU执行时间
#print(time.gmtime())
#print(time.localtime())
#struct_time=time.localtime()
#print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time))
#print(time.strptime('2018-11-23 22:00:03','%Y-%m-%d %H:%M:%S'))

# a=time.strptime('2018-11-23 22:00:03','%Y-%m-%d %H:%M:%S')
# print(a.tm_year)
# print(a.tm_mday)
# print(a.tm_wday)

#print(time.ctime())

#print(time.mktime(time.localtime()))

import datetime
print(datetime.datetime.now())


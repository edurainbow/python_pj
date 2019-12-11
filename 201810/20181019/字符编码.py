#-*-coding:utf-8-*-
#__author:"Peter"
#date:2018/10/20

#python2:
# s = '特斯拉'
# s_to_unicode = s.decode('utf-8')
# unicode_to_gbk = s_to_unicode.encode('gbk')
# print(unicode_to_gbk)

#python3:
# import sys
# print(sys.getdefaultencoding())
s = "特斯拉"
s_to_gbk = s.encode("gbk")

print(s)
print(s_to_gbk.decode("gbk"))
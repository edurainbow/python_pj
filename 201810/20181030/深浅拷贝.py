#__author:"Peter"
#date:2018/10/30

# s=[1,'alex','alvin']
# s1=[1,'alex','alvin']
# s1[0]=2
# print(s)
# print(s1)

# s=[1,'alex','alvin']
# s2=s.copy()
# print(s2)
# s2[0]=3
# print(s)
# print(s2)

# s=[[1,2],'alex','alvin']
# s3=s.copy()
# print(s3)
# # s3[1]='linuyx'
# # print(s3)
# # print(s)
# s3[0][1]=3
# print(s3)
# print(s)


# husband = ["Xiaohu",123,[15000,9000]]
# wife = husband.copy()
# wife[0] = "XiaoPang"
# wife[1] = 345
# husband[2][1] -=3000
# print(wife)


import copy
husband = ["Xiaohu",123,[15000,9000]]
xiaosan = copy.deepcopy(husband)
xiaosan[0] = "JinXin"
xiaosan[1] = 666
xiaosan[2][1] -= 1999
husband[2][1] -=3000
print(xiaosan)
print(husband)

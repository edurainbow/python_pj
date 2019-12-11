#__author:"Peter"
#date:2019/11/25
name=input("Please input name:")
age=eval(input("please input age:"))
tall=eval(input("please input tall:"))
start=input("please input start:")
pos=input("please input pos:")

if pos !="北京":
    print("地址不符合，淘汰")
else:
    if age <=40:
        print("年龄不和，淘汰")
    else:
        if tall<=170:
            print("身高不行，淘汰")
        else:
            if start == "天蝎座":
                print("星座不符合，淘汰")
            else:
                print("符合要求",name)
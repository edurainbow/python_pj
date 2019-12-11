#__author:"Peter"
#date:2018/10/14

# counter = 0
# while True:
#     if  counter >2**25:
#         break
#     counter +=1
#
#     # print("helo word")

_user="alex"
_passwd="abc123"

counter = 0
while counter < 3:
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("Wellcome %s login... " % _user)
        break
    else:
        print("Invalid username or password!")
    counter += 1
    if counter == 3:
        keep_going_choice = input("还要玩吗？[y/n]:")
        if  keep_going_choice == "y":
            counter = 0
else:
    print("要不要脸，臭流氓")

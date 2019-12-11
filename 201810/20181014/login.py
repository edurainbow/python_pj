#__author:"Peter"
#date:2018/10/14

# for i in range(1,101):
#     if i % 2 !=0:
#         print(i)

# for i in range(100):
#     if i <50 or i > 70:
#         print(i)

# for i in range(1,101,2):
#         print(i)


# _user="alex"
# _passwd="abc123"
# passed_authentication = False
#
# for i in range(3):
#     username = input("Username:")
#     password = input("Password:")
#
#     if username == _user and password == _passwd:
#         print("Wellcome %s login... " % _user)
#         passed_authentication = True
#         break
#     else:
#         print("Invalid username or password!")
# if not passed_authentication:
#     print("要不要脸，臭流氓")

_user="alex"
_passwd="abc123"


for i in range(3):
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("Wellcome %s login... " % _user)
        break
    else:
        print("Invalid username or password!")
else:
    print("要不要脸，臭流氓")
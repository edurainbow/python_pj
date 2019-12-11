#__author:"Peter"
#date:2018/11/9

#user,passwd=alex,123

login_status = False
def login():
    if login_status == False:
        username = input("username:")
        password = input("password:")
        if user == username and passwd == password:
            print("welcome...")
            home()
            login_status=True
    else:
        pass

@login
def home():
    print(welcom to home page)

@login
def finance():
    print(welcom to finance page)

@login
def book():
    print(welcom to book page)


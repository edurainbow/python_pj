#__author:"Peter"
#date:2018/10/14
name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():
    salary = int(salary)
# else:
#    # print("must input digit")
#     exit("must input digit")
#print(name,age,job,salary)

msg = '''
-----------info of %s--------
Name:%s
Age:%d
Job:%s
Salary:%d
You will be retired in %s years
-----------end----------------

'''%(name,name,age,job,salary,65-age)
print(msg)

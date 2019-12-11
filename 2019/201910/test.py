#__author:"Peter"
#date:2019/10/17

# try:
#    5/0
# except:
#     pass
#     print("Please don't do that")

# try:
#     a=5/1
#     print("Good to go!")
# except:
#     print("Please dont't do that")

# a=5
# try:
#     a = a+1
#     a=a/0
# except ZeroDivisionError:
#     print("Please don't do that")
# print(a)

# total = 19 + 9.99 + 13.97 + 20 + 15.97 + 9.97 + 10 * 2
# party = 8
# total = 13 + 14.02 + 22.35
# party = 3
# print("Receipt for your meal")
# if party >=8 :
#     total = total + total * .2
#     print("We've added the tip automatically, since your party was eight or larger.")
# print("Total:",'%.2f' % total)
# print("Thank you for dining with us today!")

# import sys
# print(sys.version)

# name = "Little Miss Muffett\n\
# Sat on Tuffet\n\
# Eating her curds and whey."
# print (name)

# import this
# first_name = "****Hannah*****"
# print (first_name.lstrip('*'))
# print(first_name.count('n'))
# print (first_name.find('a'))

# age = raw_input('your age:')
# age = int(age)
# print ('age:',age)

# from getpass import getpass
# password = getpass()
# print password


# year = raw_input("What year were you born [ex:1980]?")
# if len(year) !=4 or not year.isdigit():
#     print "I'm sorry,I don't like that number."
# else:
#     print "That's good.Moving on!"

# name = "Hannah"
# time = "morning"
# print "Good" + time + "," + name + ". How are you doing?"

# greeting = "Good {}, {}. How are you doing?"
# name = "Hannah"
# time = "morning"
# print greeting.format(time,name)

# specials_text = "Good {time}! Today's specials are: {special1} and {special2}."
# time = "afternoon"
# food1 = "spam with eggs"
# food2 = "eggs with span"
# print specials_text.format(time=time,special1=food1,special2=food2)

# breakfast_special = "Texas Omelet"
# breakfast_notes = "Contains brisket, horseradish cheddar"
# lunch_special = "Greek patty melt"
# lunch_notes = "Like the regular one, but with tzatziki sauce"
# dinner_special = "Buffalo steak"
# dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."
#
# meal_time = raw_input('Which mealtime do you want? [breakfast,lunch,dinner]')
# print 'Specials for {}:'.format(meal_time)
# if meal_time == 'breakfast':
#     print breakfast_special
#     print breakfast_notes
# elif meal_time == 'lunch':
#     print lunch_special
#     print lunch_notes
# elif meal_time == 'dinner':
#     print dinner_special
#     print dinner_notes
# else:
#     print 'Sorry,{} isn\'t valid.'.format(meal_time)

# color_list = ['red', 'blue', 'magenta', 'red', 'yellow']
# # print len(color_list)
# #print color_list.count('red')
# # print color_list.index('blue')
# print 'abc' in color_list

# toppings = []
# toppings.append('pepperoni')
# toppings.append('mushrooms')
# print toppings

# order1 = ['pizza', 'fries', 'baklava']
# order2 = ['soda', 'lasagna']
# print order1 + order2
# order1.extend(order2)
# print order1

# colors = ['red','green','yellow']
# colors[2] = 'black'
#colors.remove('green')
# colors.insert(1,'orange')
# print colors

# names =['1', '20', '3.0','4.7']
# print(names.reverse())
# print(names.sort())

# requested_classes = ['ENGL101','CS100','SPAN102']
# schedule = ['ENGL101','CS100','SPAN102']
# print requested_classes == schedule

# inventory = ['butter',
#              'tomato sauce',
#              'green beans',
#              'chicken',
#              'italian herbs',
#              'garlic',
#              'hamburger',
#              'flour',
#              'eggs',
#              'noodles']
# print "Welcom to the Inventory program!"
# item = raw_input("What item do you want to check?")
# if item in inventory:
#     print "Yes, we have that."
# else:
#     print "No, we don't have that."

# numbers = [5,2,0,20,30]
# for number in numbers:
#     if number == 0:
#         print "Ugh. You gave me a 0."
#         continue
#     new_number = 100.0/number
#     print "100/{} = {}".format(number,'%.2f' %new_number)

# cart = [50.25, 20.98, 99.99, 1.24, .84, 60.03]
# for item in cart:
#     print item
#     if item > 100:
#         print "You are going to require insurance on this order."
#         break
# else:
#     print "No insurance will be required for this order."

# age = raw_input("Please give me your age in years (eg. 30):")
# while not age.isdigit():
#     print "I'm sorry, but {} isn't valid.".format(age)
#     age = raw_input("Please give me your age in years (eg. 30):")
# print "Thanks! Your age is set to {}".format(age)

# while True :
#     text = raw_input("Give me some text, and I'll count the e's. "
#                      "Enter 'q' to quit:")
#     if text == 'q':
#         break
#     print text.count('e')

breakfast_special = "Texas Omelet"
breakfast_notes = "Contains brisket, horseradish cheddar"
lunch_special = "Greek patty melt"
lunch_notes = "Like the regular one, but with tzatziki sauce"
dinner_special = "Buffalo steak"
dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."

# while True:
#     meal_time = raw_input('Which mealtime do you want? [breakfast,lunch,dinner,q to quit]')
#     if meal_time == 'q':
#         break
#     print 'Specials for {}:'.format(meal_time)
#     if meal_time == 'breakfast':
#         print breakfast_special
#         print breakfast_notes
#     elif meal_time == 'lunch':
#         print lunch_special
#         print lunch_notes
#     elif meal_time == 'dinner':
#         print dinner_special
#         print dinner_notes
#     else:
#         print 'Sorry,{} isn\'t valid.'.format(meal_time)
# print "Goodbye!"

# fruit = ['apple', 'banana', 'mango']
# for item in fruit:
#     print 'Currently on:',item
#     if item == 'banana':
#         fruit.append('pear')

# def hello2(name):
#     print "Hello, {}".format(name)
# hello2('Hannah')

# def print_address(name,address):
#     print name
#     print address
# hospital = "INOVA Hospital"
# address = "300 Prince William Parkway\n\
# Woodbridge, VA22193"
# print_address(hospital,address)

# def print_total(customer_name, items):
#     print "Total for {}".format(customer_name)
#     total = 0
#     for item in items:
#         total = total + item
#     print "${}".format(total)
# print_total(items=[4.52, 6.31, 5.00], customer_name="Karen")

# def print_welcome(first, last, middle=''):
#     print "Welcome, {} {} {}!".format(first, middle, last)
#     print "Enjoy your stay!"
# # print_welcome(first="James", last="Grinnell")
# print_welcome(first="Katie", middle="Alison", last="Cunningham")

# def get_total(items):
#     total = 0
#     for item in items:
#         total = total + item
#     return total
# items = [2, 5, 7, 8, 2]
# items_total = get_total(items)
# print items_total

# def get_square_and_cube(number):
#     square = number ** 2
#     cube = number ** 3
#     return square, cube
# # result = get_square_and_cube(5)
# # print result
# square, cube =get_square_and_cube(3)
# print square
# print cube

# def check_year(year):
#     if len(year) != 4:
#         print "{} is invalid as a year.".format(year)
#         return
#     print "Good, that seems to work as a year!"
# check_year("2010")

# def test_args(item_one, item_two, **kwargs):
#     print item_one
#     print item_two
#     print kwargs
# test_args(item_one="hello", item_two="world", item_three="How are you?", item_four="How do you do!")

# def test_args(first, second, *args):
#     print first
#     print second
#     print args
# test_args(1,2,3,4,5)

# def print_seat(seat):
#     for item in seat:
#         print "${}".format(item)
#     print "-"*15
#     total = get_seat_total(seat)
#     print "Total:${}".format(total)
# def get_seat_total(seat):
#     total = 0
#     for dish in seat:
#         total = total + dish
#     return total
# def main():
#     seats = [[19.95],[20.45 + 3.10],[7.00/2,2.10,21.45],[7.00/2,2.10,14.99]]
#     grand_total = 0
#     for seat in seats:
#         print_seat(seat)
#         grand_total = grand_total + get_seat_total(seat)
#         print "\n"
#     print "="*15
#     print "Grand total: ${}".format(grand_total)
#
# if __name__ == '__main__':
#     main()

# def print_numbers(n):
#     print n
#     n -= 1
#     if n:
#         print_numbers(n)
#     n += 1
#     print n
# print_numbers(5)

# class MyClass(object):
#     a = 5
#     b = 2
#     c = "Hello"
# new_item = MyClass
# new_item.a = 10
# print new_item.a
# print new_item.c

# class MyClass(object):
#     a = 5
#     b = 2
#     c = "Hello"
#     def print_a(self):
#         print "Hello! Here is a: {}".format(self.a)
# my_object = MyClass()
# my_object.print_a()

# class School(object):
#     name = ''
#     address = ''
#     type = 'grade school'
#     def print_school(self):
#         print self.name
#         print self.address
#         print "Type:" + self.type
# school1 = School()
# school2 = School()
# school1.name = "Wyland Elementary"
# school1.address = "100 Pechtree Ave\nAtlanta GA"
# school2.name = "George Mason University"
# school2.address = "300 University Way\nFairfax VA"
# school2.type = "university"
# school2.print_school()

# class Student(object):
#     def __init__(self):
#         self.name = "None"
#         self.grade = "K"
#         self.district = "Orange County"
# student1 = Student()
# print student1.grade

# class Student(object):
#     def __init__(self, name = "None", grade = "K", district = "Orange Country"):
#         self.name = name
#         self.grade = grade
#         self.district = district
# student1 = Student()
# student2 = Student(name= "Byron Blaze",grade = "12", district = "Fairfax Country")
# print student1.name
# print student2.name


# class Student(object):
#     def __init__(self,name="",school="",grade=""):
#         if not name:
#             name = raw_input("What is the student's name?")
#         if not school:
#             school = raw_input("What is the student's school?")
#         if not grade:
#             grade = self.get_grade()
#         self.name = name
#         self.school = school
#         self.grade = grade
#         self.print_student()
#     def get_grade(self):
#         while True:
#             grade = raw_input("What is student's grade? [K, 1-5]")
#             if grade.lower() not in ['k','1','2','3','4','5']:
#                 print "I'm sorry,but {} isn't valid.".format(grade)
#             else:
#                 return grade
#     def print_student(self):
#         print "Name: {}".format(self.name)
#         print "School: {}".format(self.school)
#         print "Grade: {}".format(self.grade)
# def main():
#     student1 = Student()
#     student2 = Student(name="Byron Bale",grade="2",school="Minnieville")
# if  __name__ == '__main__':
#     main()

# class Student(object):
#     def __init__(self,name="",school="",grade=""):
#         if not name:
#             name = raw_input("What is the student's name?")
#         if not school:
#             school = raw_input("What is the student's school?")
#         if not grade:
#             grade = self.get_grade()
#         self.name = name
#         self.school = school
#         self.grade = grade
#         #self.print_student()
#     def get_grade(self):
#         while True:
#             grade = raw_input("What is student's grade? [K, 1-5]")
#             if grade.lower() not in ['k','1','2','3','4','5']:
#                 print "I'm sorry,but {} isn't valid.".format(grade)
#             else:
#                 return grade
#     def print_student(self):
#         print "Name: {}".format(self.name)
#         print "School: {}".format(self.school)
#         print "Grade: {}".format(self.grade)
# def print_roster(students):
#     print "Students in the system:"
#     for student in students:
#         print "*"*15
#         student.print_student()
# def main():
#     student1 = Student(name="Carrie Kale",grade="3",school="Marshall")
#     student2 = Student(name="Byron Bale",grade="2",school="Minnieville")
#     student3 = Student(name="Sarah Chandler", grade="K", school="Woodbridge")
#     students = [student1,student2,student3]
#     print_roster(students)
# if  __name__ == '__main__':
#     main()

# class MenuItem(object):
#     def __init__(self,title,cost,long_desc='',short_desc='',item_type='main'):
#         self.title = title
#         self.cost = cost
#         self.long_desc = long_desc
#         self.short_desc = short_desc
#         self.item_type = item_type
#     def change_item_type(self,item_type):
#         self.item_type = item_type
#     def change_cost(self,cost):
#         self.cost = cost
#     def change_description(self,long_desc='',short_desc=''):
#         if long_desc:
#             self.long_desc = long_desc
#         if short_desc:
#             self.short_desc = short_desc
#     def change_title(self,title):
#         self.title = title
#     def priint_item(self,desc_type='short'):
#         print "{title}... ${cost}".format(title=self.title,cost=self.cost)
#         if desc_type == 'short':
#             print self.short_desc
#         elif desc_type == 'long':
#             print self.long_desc
# class Menu(object):
#     def __index__(self,breakfast,lunch,dinner):
#         self.breakfast = breakfast
#         self.lunch = lunch
#         self.dinner = dinner
#     def print_menu(self):
#         print "Breakfast"
#         for item in self.breakfast:
#             item.print_item()
#         print
#         print "Lunch"
#         for item in self.lunch:
#             item.print_item()
#         print
#         print "Dinner"
#         for item in self.dinner:
#             item.print_item()

# class Test(object):
#     def __init__(self,one):
#         self.one = one
#     def __eq__(self, other):
#         if self.one == other.one:
#             return True
#         else:
#             return False
# a = Test(5)
# b = Test(5)
# c = Test(7)
# print a == b
# print a == c

# class Test(object):
#     def __init__(self,num):
#         self.num = num
#     def __eq__(self, other):
#         if  self.num == other.num:
#             return True
#         else:
#             return False
#     def __ne__(self, other):
#         if self.num != other.num:
#             return True
#         else:
#             return False
# a = Test(5)
# b = Test(5)
# c = Test(7)
# print a != b
# print a != c

# class Test(object):
#     def __init__(self,num):
#         self.num = num
#     def __gte__(self,other):
#         if self.num >= other.num:
#             return True
#         else:
#             return False
# alpha = Test(5)
# beta = Test(5)
# gamma = Test(6)
# print alpha >= beta
# print alpha >= gamma
# print gamma >= alpha

# class Test(object):
#     def __init__(self,word,num):
#         self.word = word
#         self.num = num
#     def __str__(self):
#         return "Values in this object:word = {word},num={num}".format(word=self.word,num=self.num)
# a = Test(word = 'Hello',num=5)
# print a

# from random import randint
# for i in range(10):
#     print randint(1,10)

# from random import randint
# frequency = {}
# for i in range(13):
#     num = randint(1,10)
#     if frequency.has_key(num):
#        frequency[num] = frequency[num] + 1
#     else:
#         frequency[num] = 1
# print frequency

# import random
# print random.randint(1,100)

# from random import random
# for i in range(10):
#     print random()

# from random import uniform
# for i in range(10):
#     print uniform(1,5)

# from   random import choice
# names = ['Hannah','Jacob','Jim','Katie','Wonderdog']
# print choice(names)

# import datetime
# from datetime import time
# lunch = time(11,30)
# datetime.time(11,30)
# #print lunch
# # print lunch.hour
# # print lunch.minute
# print "Lunch will be served at {minutes} minutes past {hour}".format(minutes=lunch.minute,hour=lunch.hour)

# import datetime
# breakfast = datetime.time(7,30)
# lunch = datetime.time(11,30)
# elevensies = datetime.time(11,30)
# print breakfast < lunch
# print elevensies == lunch

# import datetime
# hm = datetime.datetime(year=2009,day=9,month=1)
# jt = datetime.datetime(year=2001,day=14,month=4)
# print (hm-jt)

# import datetime
# week = datetime.timedelta(days=7)
# n = datetime.datetime.now()
# print n+week
# print datetime.datetime(2012,10,30,12,18,32,227051)

# import datetime
# payday = datetime.datetime(year=2011,day=31,month=5)
# period = datetime.timedelta(days=14)
# next_payday = payday + period
# print next_payday
# print datetime.date(2013,6,14)

# from datetime import datetime
# time = datetime.now()
# time_template = "Date/time:{M}/{D}/{Y} {H}:{Min}"
# print time_template.format(M=time.month,
#                            D=time.day,
#                            Y=time.year,
#                            H=time.hour,
#                            Min=time.minute)


# f = open("E:\SIP-400LOG.txt")
# print f
# user = f.readline()
# print user
# user2 = f.readline()
# user3 = f.readline()
# user4 = f.readline()
# print user
# print user2
# print user3
# print user4

# f = open('E:\SIP-400LOG.txt','w')
# f.write('SIP-400LOG.txt')
# f.close()
# f = open("E:\SIP-400LOG.txt")
# lines = f.readlines()
# for line in lines:
#     print line


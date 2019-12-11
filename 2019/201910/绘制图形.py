#__author:"Peter"
#date:2019/11/14
'''
# import turtle
# turtle.screensize(1570,817)
# turtle.write("hello天朝",font=("微软亚黑",20,"normal"))
# turtle.showturtle()
# turtle.circle(50,steps=20)
# turtle.done()
# '''
# import turtle
# turtle.screensize(1570,817)
# turtle.write("hello天朝",font=("微软亚黑",20,"normal"))
# turtle.showturtle()
#
# turtle.begin_fill()
# turtle.circle(50,steps=5)
# turtle.color("yellow")
# turtle.end_fill()
#
# #turtle.pensize(20)
# turtle.begin_fill()
# turtle.circle(50,steps=5)
# turtle.color("blue")
# turtle.end_fill()
# turtle.hideturtle()
# turtle.done()

import turtle

turtle.screensize(1570,817)
turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color('yellow')
turtle.speed(10)
#主星
turtle.begin_fill()
turtle.up()
turtle.goto(-600,220)
turtle.down()
for i in range (5):
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()

#第1颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,295)
turtle.setheading(305)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()


#第2颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,212)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第3颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,145)
turtle.setheading(5)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第4颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,90)
turtle.setheading(300)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()
turtle.hideturtle()

turtle.done()
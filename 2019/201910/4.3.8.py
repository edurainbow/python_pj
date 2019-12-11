#__author:"Peter"
#date:2019/11/15
import turtle
import math

x1,y1,x2,y2,x3,y3 = eval(input("three point:"))
a = ((x1-x2)**2 + (y1-y2)**2)**0.5
b = ((x3-x2)**2 + (y3-y2)**2)**0.5
c = ((x3-x1)**2 + (y3-y1)**2)**0.5

A = math.degrees(math.acos((b*b+c*c-a*a)/(2*b*c)))
B = math.degrees(math.acos((-b*b+c*c+a*a)/(2*a*c)))
C = math.degrees(math.acos((b*b-c*c+a*a)/(2*b*a)))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write(format(B,".2f"))
turtle.goto(x2,y2)
turtle.write(format(C,".2f"))
turtle.goto(x3,y3)
turtle.write(format(A,".2f"))
turtle.goto(x1,y1)
turtle.done()
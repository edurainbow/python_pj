#__author:"Peter"
#date:2019/11/12
import turtle
x1,y1=eval(input("请输入x1,y1"))
x2,y2=eval(input("请输入x2,y2"))
print(x1,y1)
print(x2,y2)

turtle.penup()
turtle.goto(x1,y1)
turtle.write(str(x1)+","+str(y1))
turtle.pendown()
turtle.goto(x2,y2)
turtle.write(str(x2)+","+str(y2))
turtle.goto((x1+x2)/2,(y1+y2)/2)

length=((x1-x2)**2+(y1-y2)**2)**0.5
turtle.write("长度="+str(length))
turtle.done()
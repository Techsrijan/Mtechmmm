from turtle import *
s=Turtle()
s.color("red","green")
s.left(45)
s.penup()
s.forward(200)
s.pendown()
s.right(45)
s.begin_fill()
for i in range(4):
    s.forward(100)
    s.left(90)
s.end_fill()
done()
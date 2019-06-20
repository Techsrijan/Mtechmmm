from turtle import *
s=Turtle()
lst=["red","yellow","green","blue","magenta"]
s.up()
s.goto(200,0)
for i in range(5):
    s.down()
    s.begin_fill()
    s.fillcolor(lst[i])
    s.pensize(10)
    s.circle(50)
    s.end_fill()
    s.up()
    s.bk(100)
done()
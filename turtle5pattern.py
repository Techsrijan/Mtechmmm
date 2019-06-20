from turtle import *
s=Turtle()
lst=["red","yellow","green","blue","magenta"]

for i in range(150):
    s.color(lst[i%5])
    s.pensize(i/10+1)
    s.forward(i)
    s.left(60)
done()
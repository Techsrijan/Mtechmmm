from tkinter import *

def msg(event):
    print("Good morning")

def msg1(event):
    print("Good Afternoon")


def msg2(event):
    print("Good Evening")


root =Tk()
#button=Button(root,text="click me",command=msg)
button1=Button(root,text="Left Click")
button2=Button(root,text="Middle Click")
button3=Button(root,text="Right Click")
button1.bind("<Button-1>",msg)
button1.pack()
button2.bind("<Button-2>",msg1)
button2.pack()
button3.bind("<Button-3>",msg2)
button3.pack()

#widgets
root.geometry("500x300+400+120")
root.mainloop()
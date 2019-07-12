from tkinter import *
def msg():
    print("good morning")

root =Tk()
frame=Frame(root,height=500,width=300,bg="red")
btn=Button(frame,text="Click me",bg="red",fg="white",command=msg)
#f=Frame(frame,height=200,width=100,bg="yellow")
#f.pack()
btn.pack()
frame.pack()
#widgets
root.mainloop()
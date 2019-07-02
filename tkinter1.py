from tkinter import *
root =Tk()
frame=Frame(root)

TheLabel= Label(frame,text="Enter User Name")
TheLabel.pack()
button1=Button(frame,text="Login")
button2=Button(frame,text="Register")
button3=Button(frame,text="Cancel")
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=BOTTOM)
frame.pack()
#widgets
root.mainloop()
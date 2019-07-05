from tkinter import *
root =Tk()
frame=Frame(root,height=500,width=300,bg="red")
TheLabel= Label(frame,text="Enter User Name")
TheLabel.grid(row=0,column=0)
entry =Entry(frame)
entry.grid(row=0,column=1)


TheLabel1= Label(frame,text="Enter User Pasword")
TheLabel1.grid(row=1,column=0)
entry1 =Entry(frame)
entry1.grid(row=1,column=1)


frame.pack()
#widgets
root.mainloop()
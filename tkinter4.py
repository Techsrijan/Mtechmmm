from tkinter import *
root =Tk()

TheLabel= Label(root,text="Enter User Name")
TheLabel.place(x=20,y=50)
entry =Entry(root)
entry.place(x=200,y=50)


TheLabel1= Label(root,text="Enter User Pasword")
TheLabel1.place(x=50,y=100)
entry1 =Entry(root)
entry1.place(x=200,y=200)



#widgets
root.geometry("500x300+400+120")
root.mainloop()
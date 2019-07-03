from tkinter import *
root =Tk()
#frame=Frame(root)

TheLabel= Label(root,text="Enter User Name")
TheLabel.pack()
button1=Button(root,text="Login",bg="red",fg="yellow",padx="10")
button2=Button(root,text="Register",padx=20)
button5=Button(root,text="Registerfdsfsdf")
button3=Button(root,text="Cancel")
button1.pack(side=LEFT)
#button2.pack(fill=X)
button2.pack(side=LEFT)
button3.pack(side=LEFT,fill=Y)
button5.pack()

#frame.pack()
f=Frame(root)
button4=Button(f,text="Register")
button4.pack(fill=X)
f.pack(side=BOTTOM)

#widgets
root.mainloop()
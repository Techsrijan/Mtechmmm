from tkinter import *

'''def msg():
    print("Good morning")'''


def msg(event):
    print("Good morning")
root =Tk()
#button=Button(root,text="click me",command=msg)
button=Button(root,text="click me")
button.bind("<Button-1>",msg)
button.pack()



#widgets
root.geometry("500x300+400+120")
root.mainloop()
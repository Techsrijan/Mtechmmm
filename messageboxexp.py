from tkinter import *
from tkinter import messagebox

def msg():
    #messagebox.showinfo("TESTING","Happy _Baday")
    result=messagebox.askyesnocancel("Save File","Do you want to save file")
    print(result)
    if result==True:
        print("thanks ")
    elif result==False:
        root.quit()
    #messagebox.showwarning("Save File","Do you want to save file")







root =Tk()
#button=Button(root,text="click me",command=msg)
button=Button(root,text="click me",command=msg)
button.pack()

#widgets
root.geometry("500x300+400+120")
root.mainloop()
from mmm import *
import tkinter as tk
from tkinter import *
import tkinter.font as font

def selection():

    def select():
        global temp
        a=int(sel.get())
        #print(a)
        temp=int(a)
        rot.destroy()
        func(temp)
        
        
        


    
    rot = Tk()
    rot.geometry("600x250")
    rot['background']='#99643A'
    rot.title("MMM")
    sel=IntVar()
    mylabel=Label(rot,text="how would you like to be notified?")
    mylabel.grid(row=3,column=5,columnspan=3,padx=10,pady=10)

    rb=Radiobutton(rot, text ="Call",variable=sel,value ="1",command=select)
    rb.grid(row=4,column=5)

    rb2=Radiobutton(rot, text ="SMS",variable=sel,value ="2",command=select)
    rb2.grid(row=4,column=6)

    rb3=Radiobutton(rot, text ="Both",variable=sel,value ="3",command=select)
    rb3.grid(row=4,column=10)
    rot.mainloop()
#selection()

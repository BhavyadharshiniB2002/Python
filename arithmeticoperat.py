
# arithmetic operator
import tkinter
from tkinter import *
from tkinter import messagebox

r=Tk()
r.geometry("400x400")
l1=Label(r,text="Enter the first value")
l1.grid(row=0,column=1)
l2=Label(r,text="Enter the second value")
l2.grid(row=1,column=1)
l3=Label(r,text="Result")
l3.grid(row=2,column=1)
e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    e3.delete(0,50)
    e3.insert(0,c)
def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    e3.delete(0,50)
    e3.insert(0,c)
def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    e3.delete(0,50)
    e3.insert(0,c)
def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    e3.delete(0,50)
    e3.insert(0,c)
    messagebox.showinfo("textbox","valid-successfully")

b=Button(r,text="Sub",bg="pink",command=lambda:sub())
b.grid(row=0,column=3)

b=Button(r,text="Add",bg="red",command=lambda:add())
b.grid(row=1,column=3)

b=Button(r,text="Mul",bg="green",command=lambda:mul())
b.grid(row=2,column=3)

b=Button(r,text="Div",bg="yellow",command=lambda:div())
b.grid(row=3,column=3)

r.mainloop()
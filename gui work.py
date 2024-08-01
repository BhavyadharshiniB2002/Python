#gui function
from tkinter import*
root=Tk()
root.title("welcome to the page")
frame=Frame(root,bg="red",width=600,height=400)
frame.pack()
btn=Button(frame,text="livewire")
btn.pack()
root.mainloop()
from tkinter import*
root=Tk()
root.title("welcome to the page")
root=Frame(root,bg="blue",width=200,height=300)
root.grid()
lbl=Label(root,text="are you geek")
lbl.grid()
def clicked():
    lbl.configure(text="i just got clicked")
btn=Button(root,text="click me",fg="red",command=clicked)
btn.grid()
root.mainloop()

#gui basic
import tkinter
r=tkinter.Tk()
r.title("welcome to the page")
frame=tkinter.Frame(r,bg="blue",width=600,height=400)
frame.grid()
lbl=tkinter.Label(r,text="name")
lbl.grid()
button=tkinter.Button(r,bg="red",text="google")
button.grid(column=0,row=0)
r.mainloop()

#gui fun work
from tkinter import*
root=Tk()
root.title("welcome to geeks for geeks")
root.geometry("350x200")
lbl=Label(root,text="are you a geek")
lbl.grid()
txt=Entry(root,width=10)
txt.grid(column=1,row=0)
def clicked():
    res="you wrote"+txt.get()
    lbl.configure(text=res)
btn=Button(root, text="click me",fg="red",command=clicked)
btn.grid(column=2,row=0)
root.mainloop()


#work
from tkinter import*
top=Tk()
top.title("hello world")
top.geometry("300x400")
frame=Frame(top,bg="blue")
frame.grid()
lbl=Label(top,text="name:")
lbl.grid(column=0,row=0)
lbl=Label(top,text="age:")
lbl.grid(column=0,row=1)
btn=Button(top)
btn.grid(column=1,row=0)
btn=Button(top)
btn.grid(column=1,row=1)
top.mainloop()


#img work
from tkinter import*
from PIL import ImageTk,Image
from PIL.ImageTk import PhotoImage
root=Tk()
root.geometry("700x500")
frame=Frame(root,width=600,height=400)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
img=PhotoImage(Image.open("nature.jpg"))
frame1=Frame(root,width=600,height=400)
frame1.pack()
frame1.place(anchor="w",relx=0.5,rely=0.5)
img1=PhotoImage(Image.open("flower.jpg"))
label=Button(frame,image=img)
label.pack()
label1=Button(frame,image=img1)
label1.pack()
root.mainloop()

#function work
import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password=passw_var.get()
    print("the name is:"+name)
    print("the password is:"+password)
    name_var.set("")
    passw_var.set("")
name_label=tk.Label(root,text="username",font=("cabibre",10,"bold"))
name_label.grid(row=0,column=0)
name_entry=tk.Entry(root,textvariable=name_var,font=("calibre",10,"normal"))
name_entry.grid(row=0,column=1)
passw_label=tk.Label(root,text="password",font=("calibre",10,"bold"))
passw_label.grid(row=1,column=0)
passw_entry=tk.Entry(root,textvariable=passw_var,font=("calibre",10,"normal"),show="*")
passw_entry.grid(row=1,column=1)
sub_btn=tk.Button(root,text="submit",command=submit)
sub_btn.grid(row=2,column=1)
root.mainloop()


#btn add,sub work
from tkinter import*
r=Tk()
r.geometry("400x400")
l=Label(r,text="enter the first value:")
l.grid(row=0,column=1)
l1=Label(r,text="enter the second value:")
l1.grid(row=1,column=1)
l2=Label(r,text="result:")
l2.grid(row=2,column=1)
e=Entry(r)
e.grid(row=0,column=2)
e1=Entry(r)
e1.grid(row=1,column=2)
e2=Entry(r)
e2.grid(row=2,column=2)
def add():
    a=int(e.get())
    b=int(e1.get())
    c=a+b
    e2.delete(0,END)
    e2.insert(0,c)
b=Button(r,text="add",command=lambda:add())
b.grid(row=3,column=3)
def sub():
    a=int(e.get())
    b=int(e.get())
    c=a-b
    e2.delete(0,END)
    e2.insert(0,c)
b1=Button(r,text="sub",command=lambda:sub())
b1.grid(row=4,column=3)
def mul():
    a=int(e.get())
    b=int(e.get())
    c=a*b
    e2.delete(0,END)
    e2.insert(0,c)
b2=Button(r,text="mul",command=lambda:mul())
b2.grid(row=5,column=3)
r.mainloop()



#workout uppercase
string=input("enter the string:")
if (string=="bhavyadharshini"):
    b=string[3:9].upper()
    print(b[0:2],b[2:4],b[4:7],sep='***')
else:
    print("does not correct value")

#least freq char get up
string="pythonprogramming"
freq={}
for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
least_freq=[]
for i in freq:
    if freq[i]==1:
        least_freq.append(i)
print(least_freq)




#ascending order
list=[2,6,5,9,4,1,6,0]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#workout
value=int(input("enter your value:"))
while value<5:
    value=value+1
    val=(value**3)-1
    print(val)

# using map fun 
list1=[0,1,2,3,4,5]
b=list1.copy()
b.sort()
if list1==b:
    x=map(lambda a:a*2,list1)
    print(list(x))
else:
    print("does not ascending")

#workout
rows=int(input("enter the value"))
for i in range(1,rows+1):
    for j in range(i,i+1):
        print("*"*i)

#workout
x=1
for i in range(9):
    if i<4:
        print("*"*x)
        x+=1
    elif i>3:
        print("*"*x)
        x=x-1

#workout
value="bhavya"
for i in range(6):
    if i<5:
        print(value)
        value+=value
n=int(input("enter no:"))
for i in range(n,0-1):
    for j in range(i):
        print("*",end="")
    print()

#gui work
'''from tkinter import*
root=Tk()
root.geometry("500x500")
l1=Label(root,text="name")
l1.grid(row=0,column=2)
e1=Entry(root)
e1.grid(row=0,column=3)
l2=Label(root,text="age")
l2.grid(row=1,column=2)
e2=Entry(root)
e2.grid(row=1,column=3)
l3=Label(root,text="address")
l3.grid(row=2,column=2)
e3=Entry(root)
e3.grid(row=2,column=3)
l4=Label(root,text="email")
l4.grid(row=3,column=2)
e4=Entry(root)
e4.grid(row=3,column=3)
l5=Label(root,text="phoneno")
l5.grid(row=4,column=2)
e5=Entry(root)
e5.grid(row=4,column=3)
l6=Label(root,text="marks")
l6.grid(row=5,column=2)
e6=Entry(root)
e6.grid(row=5,column=3)
l7=Label(root,text="gender")
l7.grid(row=6,column=2)
e7=Entry(root)
e7.grid(row=6,column=3)
var=IntVar()
Radiobutton(root,text="male",variable=var,value=5).grid(row=7,sticky=W)
Radiobutton(root,text="female",variable=var,value=2).grid(row=8,sticky=W)
def note():
    l11=e1.get()
    l12=e2.get()
    l13=e3.get()
    l14=e4.get()
    l15=e5.get()
    l16=e6.get()
    l17=e7.get()
    gen=""
    if var==1:
       gen="male"
    else:
       gen="female"
    f=open("file.txt","a")
    f.write(l11+" "+l12+" "+l13+" "+l14+" "+l15+" "+l16+" "+l17+" "+gen)
b=Button(root,text="submit",command=note)
b.grid(row=8,column=4)
root.mainloop()'''

#gui work
'''from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("login form")
root.geometry("500x500")
l1=Label(root,text="username")
l1.place(relx=0.1,rely=0.2)
e=Entry(root)
e.place(relx=0.3,rely=0.2)
l2=Label(root,text="password")
l2.place(relx=0.1,rely=0.3)
e1=Entry(root)
e1.place(relx=0.3,rely=0.3)
def data():
    l1=e.get()
    l2=e1.get()
    username=""
    if username=="bhavya":
        print("login successfuly")
    else:
        print("incorrect")
    f=open("user.txt","a")
    f.write(l1+""+l2+"")
b=Button(root,text="submit",command=data)
b.place(relx=0.3,rely=0.5)
root.mainloop()'''

#gui
'''import tkinter
top=tkinter.Tk()
top.mainloop()
from tkinter import*
root=Tk()
frame=Frame(root,bg="red",width=500,height=400)
f=Button(root,bg="blue")
f.pack()
frame.pack()
root.mainloop()'''
'''
import tkinter
t=tkinter.Tk()
f1=tkinter.Frame(t)
f2=tkinter.Frame(t)
l=tkinter.Label(f1,text="hello",bg="blue")
l.pack()
b=tkinter.Button(f2,text="livewire")
b.pack()
f1.pack(padx=50,pady=90)
f2.pack(padx=60,pady=50)
t.mainloop()'''




    
    






    






    










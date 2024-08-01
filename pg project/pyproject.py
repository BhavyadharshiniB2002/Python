from tkinter import*
from tkinter import messagebox
root=Tk()
l1=Label(root,text="Name").place(relx=0.1,rely=0.8)
l2=Label(root,text="Age").place(relx=0.2,rely=0.8)
l3=Label(root,text="Phone No").place(relx=0.3,rely=0.8)
l4=Label(root,text="Aadhar No").place(relx=0.4,rely=0.8)
l5=Label(root,text="Address").place(relx=0.5,rely=0.8)
l6=Label(root,text="Course").place(relx=0.0,rely=0.8)

e1=Entry(root).place(relx=0.0,rely=0.9)
e2=Entry(root).place(relx=0.0,rely=0.9)
e3=Entry(root).place(relx=0.0,rely=0.9)
e4=Entry(root).place(relx=0.0,rely=0.9)
e5=Entry(root).place(relx=0.0,rely=0.9)
e6=Entry(root).place(relx=0.6,rely=0.5)

c1=IntVar()
c2=IntVar()
Checkbutton(root,text="Male",variable=c1).place(relx=0.0,rely=0.8)
Checkbutton(root,text="Female",variable=c2).place(relx=0.6,rely=0.9)

lb=Listbox(root)
lb.insert(1,"python")
lb.insert(2,"java")
lb.insert(3,"c++")
lb.insert(4,"fullstack")
lb.place(relx=0.0,rely=0.9)
root.mainloop()



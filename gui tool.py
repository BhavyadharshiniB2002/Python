
#canvas
from tkinter import*
master=Tk()
master.title("welcome to my page")
w=Canvas(master,width=40,height=60)
w.pack()
canvas_height=100
canvas_width=500
y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
master.mainloop()


#checkbutton
from tkinter import*
master=Tk()
var1=IntVar()
Checkbutton(master,text="male",variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master,text="female",variable=var2).grid(row=1,sticky=W)
master.mainloop()

#entry
from tkinter import*
master=Tk()
Label(master,text="first name").grid(row=0)
Label(master,text="last name").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
master.mainloop()

#Frame
from tkinter import*
root=Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame,text="red",fg="red")
redbutton.pack(side=LEFT)
greenbutton=Button(frame,text="Brown",fg="brown",)
greenbutton.pack(side=LEFT)
bluebutton=Button(frame,text="blue",fg="blue")
bluebutton.pack(side=LEFT)
blackbutton=Button(bottomframe,text="black",fg="black")
blackbutton.pack(side=LEFT)
root.mainloop()

#listbox
from tkinter import*
top=Tk()
top.title("welcome to page")
frame=Frame(top,bg="red")
frame.pack()
lb=Listbox(top)
lb.insert(1,"python")
lb.insert(2,"java")
lb.insert(3,"database")
lb.insert(4,"anyother")
lb.pack()
lbl=Label(top,text="i")
top.mainloop()

#menu
from tkinter import*
root=Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="file",menu=filemenu)
filemenu.add_cascade(label="new")
filemenu.add_command(label="open")
filemenu.add_separator()
filemenu.add_command(label="exit",command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label="help",menu=helpmenu)
helpmenu.add_command(label="about")
root.mainloop()


#messagebox
from tkinter import*
from tkinter import messagebox
main=Tk()
ourmessage="this is our Message"
messagevar=Message(main,text=ourmessage)
messagevar.config(bg="lightgreen")
messagevar.pack()
main.mainloop()


# #radio button
from tkinter import*
root=Tk()
v=IntVar()
Radiobutton(root,text="gfg",variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="mit",variable=v,value=2).pack(anchor=W)
root.mainloop()


#scale
from tkinter import*
root=Tk()
w=Scale(root,from_=0,to=42)
w.pack()
w=Scale(root,from_=0,to=200,orient=HORIZONTAL)
w.pack()
root.mainloop()
from tkinter import*
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END,"livewire"+str(line))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
root.mainloop()


#text
from tkinter import*
root=Tk()
T=Text(root,height=2,width=30)
T.pack()
T.insert(END,"monolisa is the\n one of famous printing\n")
root.mainloop()


#top level
from tkinter import*
root=Tk()
root.title("keerthi")
top=Toplevel()
top.title("python")
top.mainloop()


#spinbox
from tkinter import*
master=Tk()
w=Spinbox(master,from_=0,to=10)
w.pack()
mainloop()


#image
from tkinter import*
from PIL import ImageTk,Image
from PIL.ImageTk import PhotoImage
win=Tk()
win.geometry("700x500")
frame=Frame(win,width=600,height=400)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
img=PhotoImage(Image.open("nature.jpg"))
label=Button(frame,image=img)
label.pack()
win.mainloop()

#radiobutton
from tkinter import*
def sel():
    selection="you selected the option"+str(var.get())
    Label.config(text=selection)
root=Tk()
var=IntVar()
r1=Radiobutton(root,text="option1",variable=var,value=1,command=sel)
r1.pack()
r2=Radiobutton(root,text="option2",variable=var,value=2,command=sel)
r2.pack()
r3=Radiobutton(root,text="option3",variable=var,value=3,command=sel)
r3.pack()
label=Label(root)
label.pack()
root.mainloop()


#checkbutton
from tkinter import*
r=Tk()
var=IntVar()
c=Checkbutton(r,text="new1",variable=var).pack()
var2=IntVar()
c1=Checkbutton(r,text="new2",variable=var2).pack()
var3=IntVar()
c2=Checkbutton(r,text="new3",variable=var3).pack()
r.mainloop()


#combobox
from tkinter import*
from tkinter import ttk
root=Tk()
root.title("combobox")
root.geometry("300x300")
combo=ttk.Combobox(root,values=(["option1"],["option2"],["option3"],["option4"],["option5"]))
combo.pack()
def option_selected(event):
    selected_option=combo.get()
    print("you selected:",selected_option)
combo.bind("<<<combobox selected>>",option_selected)
root.mainloop()


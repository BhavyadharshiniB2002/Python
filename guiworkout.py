#work out
s=input('enter the username: ')
k=(input('enter the passwod: '))
f=open("emp.txt","r")
lines=f.read().split("\n")
print(lines)
for line in lines:
    data=line.split("\t")
    print(data)
    if data[0]==s:
        if data[2]==k:
            print("username",data[0])
            print("password",data[2])
            break
        
else:
    print("no")
      
#gui workout
from tkinter import *
root=Tk()
text=Text(root,height=2,width=30)
text.insert(INSERT,"hello....")
text.insert(END,"kitty....")
text.pack()
b=Button(root,text='click')
b.pack()
text.tag_add("here","1.0","1.4")
text.tag_add('start','1.8','1.10')
text.tag_config("here",background="green",foreground="violet")
text.tag_config('start',background='blue',foreground='yellow')
root.mainloop()
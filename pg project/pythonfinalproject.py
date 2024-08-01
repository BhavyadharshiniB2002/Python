from tkinter import*
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
root=Tk()
root.geometry("600x600")
# root.destroy()
root.attributes('-fullscreen',True)
f=Frame(root,width=1500,height=50,bg="purple")
f.pack()
font_label=font.Font(weight="bold",family="Times New Roman",size=20)
l=Label(root,text="ONLINE SHOPPING",font=font_label)
l.place(relx=0.5,rely=0.0)
img=ImageTk.PhotoImage(Image.open('shop.jpg'))
l1=Label(f,image=img)
l1.place(relx=0.0,rely=0.8)
root.mainloop()

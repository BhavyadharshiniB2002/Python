from tkinter import*
from tkinter import font,messagebox
from PIL import ImageTk, Image
   
def cust_regis(root):
    root.destroy()
    root=Tk()
    root.geometry("500x500")
    root.attributes('-fullscreen',True)
    f=Frame(root,height=1500,width=1500)
    f.pack()
    img=ImageTk.PhotoImage(Image.open('onlineshop.jpg'))
    l1=Label(f,image=img)
    l1.place(relx=0.0,rely=0.0)
    label_font=font.Font(weight="bold",family="Calibri",size=20)
    label=Label(root,text="CUSTOMER REGISTRATION",font=label_font,bg="blue",fg="white")
    label.place(relx=0.34,rely=0.1)
    l=Label(root,text="Name" ,fg="black",font=label_font)
    l.place(relx=0.3,rely=0.2)
    l1=Label(root,text="Email Id",fg="black",font=label_font)
    l1.place(relx=0.3,rely=0.3)
    l2=Label(root,text="Mobile No",fg="black",font=label_font)
    l2.place(relx=0.3,rely=0.4)
    l3=Label(root,text="Orders",fg="black",font=label_font)
    l3.place(relx=0.3,rely=0.5)
    l4=Label(root,text="Wishlist",fg="black",font=label_font)
    l4.place(relx=0.3,rely=0.6)
    e=Entry(root)
    e.place(relx=0.5,rely=0.2,width=200,height=40)
    e1=Entry(root,)
    e1.place(relx=0.5,rely=0.3,width=200,height=40)
    e2=Entry(root)
    e2.place(relx=0.5,rely=0.4,width=200,height=40)
    e3=Entry(root)
    e3.place(relx=0.5,rely=0.5,width=200,height=40)
    e4=Entry(root)
    e4.place(relx=0.5,rely=0.6,width=200,height=40)
   
    def online(root):
        f=open('online.txt','a')
        f.write(str(e.get()))
        f.write("\n")
        f.write(str(e1.get()))
        f.write("\t")
        f.write(str(e2.get()))
        f.write("\t")
        f.write(str(e3.get()))
        f.write("\t")
        f.write(str(e4.get()))
        f.write("\n")
    b=Button(root,text="REGISTER",font=label_font,bg="green",fg="white",command=lambda:online(root))
    b.place(relx=0.42,rely=0.75)    
    root.mainloop()  

def start(root):
    root.destroy()
    root=Tk()
    root.geometry("500x500")
    root.attributes('-fullscreen',True)
    f=Frame(root,height=1500,width=1500,bg="pink")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l=Label(root,text=" ***BEST QUALITY SHOPPING***",fg="black",font=label_font,bg="pink")
    l.place(relx=0.37,rely=0.1)
    l1=Label(root,text=" * Lowest Prices",fg="black",font=label_font,bg="pink")
    l1.place(relx=0.2,rely=0.25)
    l2=Label(root,text=" * Free Delivery",fg="black",font=label_font,bg="pink")
    l2.place(relx=0.4,rely=0.25)
    l3=Label(root,text=" * Cash On Delivery",fg="black",font=label_font,bg="pink")
    l3.place(relx=0.58,rely=0.25)
    l4=Label(root,text=" * Easy Returns",fg="black",font=label_font,bg="pink")
    l4.place(relx=0.8,rely=0.25)
    img1=ImageTk.PhotoImage(Image.open('kurtii.jpg'))
    l=Label(f,image=img1)
    l.place(relx=0.1,rely=0.35)
    img2=ImageTk.PhotoImage(Image.open('menn.jpg'))
    l1=Label(f,image=img2)
    l1.place(relx=0.34,rely=0.35)
    img3=ImageTk.PhotoImage(Image.open('kid.jpg'))
    l2=Label(f,image=img3)
    l2.place(relx=0.5,rely=0.35)
    img4=ImageTk.PhotoImage(Image.open('homess.jpg'))
    l2=Label(f,image=img4)
    l2.place(relx=0.67,rely=0.37)
    b1=Button(f,text="Womens's Store",bg="purple",fg="yellow",font=label_font,command=lambda:women_store(root))
    b1.place(relx=0.14,rely=0.75)
    b2=Button(f,text="Mens's Store",bg="purple",fg="yellow",font=label_font,command=lambda:men_store(root))
    b2.place(relx=0.35,rely=0.75)
    b3=Button(f,text="Kid's Store",bg="purple",fg="yellow",font=label_font,command=lambda:kid_store(root))
    b3.place(relx=0.53,rely=0.75)
    b4=Button(f,text="Home Essential",bg="purple",fg="yellow",font=label_font,command=lambda:home_store(root))
    b4.place(relx=0.75,rely=0.75)
    f.pack()
    root.mainloop(root)


    



   
def cust_login(root):
    root.destroy()
    root=Tk()
    root.geometry("500x500")
    root.attributes('-fullscreen',True)
    f=Frame(root,height=1500,width=1500)
    f.pack()
    img=ImageTk.PhotoImage(Image.open('onlineshop3.jpg'))
    l=Label(f,image=img)
    l.place(relx=0.0,rely=0.0)
    label_font=font.Font(weight="bold",family="Calibri",size=20)
    label=Label(root,text="CUTOMER LOGIN",font=label_font,bg="green",fg="white")
    label.place(relx=0.42,rely=0.1)
    l=Label(root,text="User Id",fg="black",font=label_font)
    l.place(relx=0.33,rely=0.3)
    l1=Label(root,text="Password",fg="black",font=label_font)
    l1.place(relx=0.33,rely=0.5)
    e=Entry(root)
    e.place(relx=0.5,rely=0.3,width=200,height=40)
    e1=Entry(root)
    e1.place(relx=0.5,rely=0.5,width=200,height=40)
    b=Button(root,text="LOGIN",font=label_font,bg="green",fg="white",command=lambda:start(root))
    b.place(relx=0.46,rely=0.7)


    
#     def cust_login(m1,n1):
#         m1=e.get()
#         n1=e1.get()
#         f=open("online.txt","r")
#         time=f.read()
#         lines=time.split("\n")
#         for line in lines:
#             info=line.split()
#             if info[0]==m1 and info[1]==n1:
#                 print("login")
#                 messagebox.showinfo("Login","login successfully")

#                 def info():
#                     info=open("online.txt","a")
#                     info=info.read()
#                 info()

                
#                 break
#             else:
#                 print("invaild")
#                 messagebox.showinfo("hello","invaild")
#                 break


     
# def cust_login1(a,b,root):
#     root.destroy()
#     if(a=="user" and b=="user"):
#         cust_regis(root)
#     else:
#         print("invalid username or password")   


   
#     root.mainloop()


# def start(root):
#     root.destroy()
#     root=Tk()
#     root.geometry("500x500")
#     root.attributes('-fullscreen',True)
#     f=Frame(root,height=1500,width=1500,bg="pink")
#     label_font=font.Font(weight="bold",family="Times New Roman",size=20)
#     l=Label(root,text=" ***BEST QUALITY SHOPPING***",fg="black",font=label_font,bg="pink")
#     l.place(relx=0.37,rely=0.1)
#     l1=Label(root,text=" * Lowest Prices",fg="black",font=label_font,bg="pink")
#     l1.place(relx=0.2,rely=0.25)
#     l2=Label(root,text=" * Free Delivery",fg="black",font=label_font,bg="pink")
#     l2.place(relx=0.4,rely=0.25)
#     l3=Label(root,text=" * Cash On Delivery",fg="black",font=label_font,bg="pink")
#     l3.place(relx=0.58,rely=0.25)
#     l4=Label(root,text=" * Easy Returns",fg="black",font=label_font,bg="pink")
#     l4.place(relx=0.8,rely=0.25)
#     img1=ImageTk.PhotoImage(Image.open('kurtii.jpg'))
#     l=Label(f,image=img1)
#     l.place(relx=0.1,rely=0.35)
#     img2=ImageTk.PhotoImage(Image.open('menn.jpg'))
#     l1=Label(f,image=img2)
#     l1.place(relx=0.34,rely=0.35)
#     img3=ImageTk.PhotoImage(Image.open('kid.jpg'))
#     l2=Label(f,image=img3)
#     l2.place(relx=0.5,rely=0.35)
#     img4=ImageTk.PhotoImage(Image.open('homess.jpg'))
#     l2=Label(f,image=img4)
#     l2.place(relx=0.67,rely=0.37)
#     b1=Button(f,text="Womens's Store",bg="purple",fg="yellow",font=label_font,command=lambda:women_store(root))
#     b1.place(relx=0.14,rely=0.75)
#     b2=Button(f,text="Mens's Store",bg="purple",fg="yellow",font=label_font,command=lambda:men_store(root))
#     b2.place(relx=0.35,rely=0.75)
#     b3=Button(f,text="Kid's Store",bg="purple",fg="yellow",font=label_font,command=lambda:kid_store(root))
#     b3.place(relx=0.53,rely=0.75)
#     b4=Button(f,text="Home Essential",bg="purple",fg="yellow",font=label_font,command=lambda:home_store(root))
#     b4.place(relx=0.75,rely=0.75)
#     f.pack()
#     root.mainloop(root)
   
   
def home_store(root):
    root.destroy()
    root=Tk()
    root.geometry("500x500")
    root.attributes('-fullscreen',True)
    f=Frame(root,height=1500,width=1500,bg="gray")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)  
    label=Label(root,text="Home's Store",font=label_font,bg="orange")
    label.place(relx=0.23,rely=0.1)
    label1=Label(root,text="Kid's Store",font=label_font,bg="orange")
    label1.place(relx=0.5,rely=0.1)
    f1=Frame(root,height=530,width=500,bg="pink")
    f1.place(relx=0.1,rely=0.2)
    img=ImageTk.PhotoImage(Image.open('furnit.jpg'))
    l1=Label(f1,image=img)
    l1.place(relx=0.13,rely=0.06)
    img1=ImageTk.PhotoImage(Image.open('decor1.jpg'))
    l2=Label(f1,image=img1)
    l2.place(relx=0.6,rely=0.06)
    img2=ImageTk.PhotoImage(Image.open('dining.jpg'))
    l3=Label(f1,image=img2)
    l3.place(relx=0.13,rely=0.53)
    img3=ImageTk.PhotoImage(Image.open('cook.jpg'))
    l4=Label(f1,image=img3)
    l4.place( relx=0.57,rely=0.5)
    b1=Button(f1,text="Furnishing",font=label_font,bg="purple",fg="yellow")
    b1.place(relx=0.19,rely=0.37)
    b2=Button(f1,text="Home Decor",font=label_font,bg="purple",fg="yellow")
    b2.place(relx=0.6,rely=0.37)
    b3=Button(f1,text="Dining",font=label_font,bg="purple",fg="yellow")
    b3.place(relx=0.65,rely=0.86)
    b4=Button(f1,text="CookWare",font=label_font,bg="purple",fg="yellow")
    b4.place(relx=0.2,rely=0.86)
    f.pack()
    # f2=Frame(root,width=500,height=500,bg="pink")
    # f2.place(relx=0.55,rely=0.2)
    # def kid_store(root):
    f2=Frame(root,width=500,height=530,bg="pink")

        # root.destroy()
        # root=Tk()
        # root.geometry("500x500")
        # root.attributes('-fullscreen',True)
    img4=ImageTk.PhotoImage(Image.open('kids1.jpg'))
    lbl1=Label(f2,image=img4)
    lbl1.place(relx=0.15,rely=0.04)
    img5=ImageTk.PhotoImage(Image.open('toys.jpg'))
    lbl2=Label(f2,image=img5)
    lbl2.place(relx=0.45,rely=0.07)
    img6=ImageTk.PhotoImage(Image.open('kid health.jpg'))
    lbl3=Label(f2,image=img6)
    lbl3.place(relx=0.15,rely=0.55)
    img7=ImageTk.PhotoImage(Image.open('kid acces.jpg'))
    lbl4=Label(f2,image=img7)
    lbl4.place(relx=0.55,rely=0.52)
    btn1=Button(f2,text="Clothess",font=label_font,bg="purple",fg="yellow")
    btn1.place(relx=0.2,rely=0.44)
    btn2=Button(f2,text="Toys",font=label_font,bg="purple",fg="yellow")
    btn2.place(relx=0.61,rely=0.37)
    btn3=Button(f2,text="Accessories",font=label_font,bg="purple",fg="yellow")
    btn3.place(relx=0.58,rely=0.87)
    btn4=Button(f2,text="Health Care",font=label_font,bg="purple",fg="yellow")
    btn4.place(relx=0.18,rely=0.87)
    # btn4=Button(f,text="Kid's Store",bg="purple",fg="yellow",font=label_font,command=lambda:kid_store(root))
    # btn4.place(relx=0.53,rely=0.75)
    f2.place(relx=0.55,rely=0.2)
    root.mainloop()
    # root.destroy()
    # root=Tk()
    # root.geometry("500x500")
    # root.attributes('-fullscreen',True)
    # f=Frame(root,height=1500,width=1500,bg="violet")
    # label_font=font.Font(weight="bold",family="Times New Roman",size=20) 
    # img=ImageTk.PhotoImage(Image.open('kids1.jpg'))
    # l1=Label(f,image=img)
    # l1.place(relx=0.25,rely=0.04)
    # img1=ImageTk.PhotoImage(Image.open('toys.jpg'))
    # l2=Label(f,image=img1)
    # l2.place(relx=0.45,rely=0.04)
    # img2=ImageTk.PhotoImage(Image.open('kid health.jpg'))
    # l3=Label(f,image=img2)
    # l3.place(relx=0.25,rely=0.52)
    # img3=ImageTk.PhotoImage(Image.open('kid acces.jpg'))
    # l4=Label(f,image=img3)
    # l4.place( relx=0.57,rely=0.52)
    # b1=Button(root,text="Clothess",font=label_font,bg="purple",fg="yellow")
    # b1.place(relx=0.28,rely=0.44)
    # b2=Button(root,text="Toys",font=label_font,bg="purple",fg="yellow")
    # b2.place(relx=0.61,rely=0.44)
    # b3=Button(root,text="Accessories",font=label_font,bg="purple",fg="yellow")
    # b3.place(relx=0.62,rely=0.92)
    # b4=Button(root,text="Health Care",font=label_font,bg="purple",fg="yellow")
    # b4.place(relx=0.33,rely=0.92)
    # f.pack()
  

    # root.mainloop()

   
# def kid_store(root):
#     root.destroy()
#     root=Tk()
#     root.geometry("500x500")
#     root.attributes('-fullscreen',True)
#     f=Frame(root,height=1500,width=1500,bg="violet")
#     label_font=font.Font(weight="bold",family="Times New Roman",size=20) 
#     img=ImageTk.PhotoImage(Image.open('kids1.jpg'))
#     l1=Label(f,image=img)
#     l1.place(relx=0.25,rely=0.04)
#     img1=ImageTk.PhotoImage(Image.open('toys.jpg'))
#     l2=Label(f,image=img1)
#     l2.place(relx=0.45,rely=0.04)
#     img2=ImageTk.PhotoImage(Image.open('kid health.jpg'))
#     l3=Label(f,image=img2)
#     l3.place(relx=0.25,rely=0.52)
#     img3=ImageTk.PhotoImage(Image.open('kid acces.jpg'))
#     l4=Label(f,image=img3)
#     l4.place( relx=0.57,rely=0.52)
#     b1=Button(root,text="Clothess",font=label_font,bg="purple",fg="yellow")
#     b1.place(relx=0.28,rely=0.44)
#     b2=Button(root,text="Toys",font=label_font,bg="purple",fg="yellow")
#     b2.place(relx=0.61,rely=0.44)
#     b3=Button(root,text="Accessories",font=label_font,bg="purple",fg="yellow")
#     b3.place(relx=0.62,rely=0.92)
#     b4=Button(root,text="Health Care",font=label_font,bg="purple",fg="yellow")
#     b4.place(relx=0.33,rely=0.92)
#     f.pack()
#     root.mainloop()




    
def menandwomen_store(root):
    root.destroy()
    root=Tk()
    root.geometry("500x500")
    root.attributes('-fullscreen',True)
    f=Frame(root,height=1500,width=1500,bg="light green")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20) 

    f1=Frame(root,height=500,width=500,bg="skyblue")
    f1.place(relx=0.1,rely=0.2)
    f.pack() 
    
    f2=Frame(root,height=500,width=500,bg="skyblue")
    f2.place(relx=0.5,rely=0.2)
    f.pack() 

    img=ImageTk.PhotoImage(Image.open('kurtis.jpg'))
    l1=Label(f1,image=img)
    l1.place(relx=0.17,rely=0.08)
    img1=ImageTk.PhotoImage(Image.open('saree4.jpg'))
    l2=Label(f1,image=img1)
    l2.place(relx=0.58,rely=0.08)
    img2=ImageTk.PhotoImage(Image.open('womenaccess1.jpg'))
    l3=Label(f1,image=img2)
    l3.place(relx=0.15,rely=0.56)
    img3=ImageTk.PhotoImage(Image.open('foot2.jpg'))
    l5=Label(f1,image=img3)
    l5.place(relx=0.70,rely=0.56)

    b1=Button(root,text="Kurtisss",font=label_font,bg="purple",fg="yellow")
    b1.place(relx=0.16,rely=0.47)
    b2=Button(root,text="Sarees",font=label_font,bg="purple",fg="yellow")
    b2.place(relx=0.32,rely=0.47)
    b3=Button(root,text="Accessories",font=label_font,bg="purple",fg="yellow")
    b3.place(relx=0.18,rely=0.78)
    b6=Button(root,text="Foot wear",font=label_font,bg="purple",fg="yellow")
    b6.place(relx=0.36,rely=0.78)

    img4=ImageTk.PhotoImage(Image.open('tshi.jpg'))
    l1=Label(f2,image=img4)
    l1.place(relx=0.17,rely=0.08)
    img5=ImageTk.PhotoImage(Image.open('jeans.jpg'))
    l2=Label(f2,image=img5)
    l2.place(relx=0.58,rely=0.08)
    img6=ImageTk.PhotoImage(Image.open('menaccesss.jpg'))
    l3=Label(f2,image=img6)
    l3.place(relx=0.15,rely=0.56)
    img7=ImageTk.PhotoImage(Image.open('foot.jpg'))
    l5=Label(f2,image=img7)
    l5.place(relx=0.70,rely=0.56)

    b1=Button(root,text="Top Wear",font=label_font,bg="purple",fg="yellow")
    b1.place(relx=0.56,rely=0.47)
    b2=Button(root,text="Bottom Wear",font=label_font,bg="purple",fg="yellow")
    b2.place(relx=0.71,rely=0.47)
    b3=Button(root,text="Accessories",font=label_font,bg="purple",fg="yellow")
    b3.place(relx=0.56,rely=0.78)
    b5=Button(root,text="Foot Wear",font=label_font,bg="purple",fg="yellow")
    b5.place(relx=0.75,rely=0.78)
    f.pack()


    root.mainloop()


# def start(root):
#     root.destroy()
#     root=Tk()
#     root.geometry("500x500")
#     root.attributes('-fullscreen',True)
#     f=Frame(root,height=1500,width=1500,bg="pink")
#     label_font=font.Font(weight="bold",family="Times New Roman",size=20)
#     l=Label(root,text=" ***BEST QUALITY SHOPPING***",fg="black",font=label_font,bg="pink")
#     l.place(relx=0.37,rely=0.1)
#     l1=Label(root,text=" * Lowest Prices",fg="black",font=label_font,bg="pink")
#     l1.place(relx=0.2,rely=0.25)
#     l2=Label(root,text=" * Free Delivery",fg="black",font=label_font,bg="pink")
#     l2.place(relx=0.4,rely=0.25)
#     l3=Label(root,text=" * Cash On Delivery",fg="black",font=label_font,bg="pink")
#     l3.place(relx=0.58,rely=0.25)
#     l4=Label(root,text=" * Easy Returns",fg="black",font=label_font,bg="pink")
#     l4.place(relx=0.8,rely=0.25)
#     img1=ImageTk.PhotoImage(Image.open('kurtii.jpg'))
#     l=Label(f,image=img1)
#     l.place(relx=0.1,rely=0.35)
#     img2=ImageTk.PhotoImage(Image.open('menn.jpg'))
#     l1=Label(f,image=img2)
#     l1.place(relx=0.34,rely=0.35)
#     img3=ImageTk.PhotoImage(Image.open('kid.jpg'))
#     l2=Label(f,image=img3)
#     l2.place(relx=0.5,rely=0.35)
#     img4=ImageTk.PhotoImage(Image.open('homess.jpg'))
#     l2=Label(f,image=img4)
#     l2.place(relx=0.67,rely=0.37)
#     b1=Button(f,text="Womens's Store",bg="purple",fg="yellow",font=label_font,command=lambda:women_store(root))
#     b1.place(relx=0.14,rely=0.75)
#     b2=Button(f,text="Mens's Store",bg="purple",fg="yellow",font=label_font,command=lambda:men_store(root))
#     b2.place(relx=0.35,rely=0.75)
#     b3=Button(f,text="Kid's Store",bg="purple",fg="yellow",font=label_font,command=lambda:kid_store(root))
#     b3.place(relx=0.53,rely=0.75)
#     b4=Button(f,text="Home Essential",bg="purple",fg="yellow",font=label_font,command=lambda:home_store(root))
#     b4.place(relx=0.75,rely=0.75)
#     f.pack()
#     root.mainloop(root)




def home():
    root=Tk()
    root.geometry("500x500")
    root.attributes('-fullscreen',True)
    f=Frame(root,width=1500,height=50,bg="purple")
    f.pack()
    label_font=font.Font(weight="bold",family="Calibri",size=30)
    l=Label(root,text="ONLINE SHOPPING",bg="purple",fg="yellow",font=label_font)
    l.place(relx=0.4,rely=0.0)
    f1=Frame(root,width=1500,height=1500,bg="purple")
    f1.pack()
    img=ImageTk.PhotoImage(Image.open('shops.jpg'))
    l=Label(f1,image=img)
    l.place(relx=0.0,rely=0.00)
    label_font1=font.Font(weight="bold",family="Calibri",size=20)
    b=Button(f1,text="CUSTOMER REGISTRATION",bg="purple",fg="yellow",font=label_font1,command=lambda:cust_regis(root))
    b.place(relx=0.03,rely=0.2)
    b=Button(f1,text="CUSTOMER LOGIN",bg="purple",fg="yellow",font=label_font1,command=lambda:cust_login(root))
    b.place(relx=0.03,rely=0.4)
    b=Button(f1,text="CLOSE",bg="purple",fg="yellow",font=label_font1,command=lambda:exit(root))
    b.place(relx=0.03,rely=0.6)
    root.mainloop()
home()

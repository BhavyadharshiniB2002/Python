from tkinter import*
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
import requests
def get_live_train_status(train_no,root):
    root.destroy()
    root=Tk()
    root.geometry("500x500")
    base_url="https://rappid.in/apis/train.php?train_no={}".format(train_no)
    response=requests.get(base_url)
    train_status=response.json()
    # train_status=get_live_train_status(trainno)
    Label(root,text="******************************").pack()
    Label(root,text="\t\t train name:"+train_status["train_name"]).pack()
    Label(root,text="******************************").pack()
    for station_info in train_status["data"]:
        if station_info["is_current_station"]:
            l=Label(root,text="now station\t\t\t\t:"+station_info["station name"]).pack()
            l1=Label(root,text="distance from the starting\t:"+station_info["distance"]).pack()
            l2=Label(root,text="timing\t\t\t\t\t:"+station_info["timing"]).pack()
            l3=Label(root,text="platform no\t\t\t\t:"+station_info["platform no"]).pack()
            l3=Label(root,text="delay\t\t\t\t:"+station_info["delay"]).pack()
            l4=Label(root,text="halt timing\t\t\t\t:"+station_info["halt"]).pack()
    else:
        l5=Label(root,text=station_info["station_name"]).pack()
        l6=Label(root,text="****************************").pack()
        l7=Label(root,text="\t\tmessage\t\t:"+train_status["message"]).pack()
        l8=Label(root,text="\t\tmessage updated:"+train_status["updated_time"]).pack()
        l9=Label(root,text="******************************").pack()
def live_train():  
    root=Tk()
    root.geometry("500x500")
    root.attributes('-fullscreen',True)
    frame=Frame(root,width=1500,height=50,bg="violet")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=25)
    label=Label(root,text="Train Location",font=label_font,fg="black",bg="violet")
    label.place(relx=0.45,rely=0.00)
    f1=Frame(root,width=1500,height=50,bg="violet")
    f1.place(relx=0.40,rely=0.2)
    img=ImageTk.PhotoImage(Image.open("train.jpg"))
    l=Label(f1,image=img)
    l.pack()
    label2=Label(root,text="Train no",font=label_font,bg="sky blue",fg="black")
    label2.place(relx=0.40,rely=0.7)
    e1=Entry(root)
    e1.place(relx=0.52,rely=0.7,width=150,height=40)
    button=Button(root,text="click",bg="sky blue",fg="black",font=label_font,command=lambda:get_live_train_status(e1.get(),root))
    button.place(relx=0.45,rely=0.8)
    root.mainloop()
live_train()






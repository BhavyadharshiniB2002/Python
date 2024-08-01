from tkinter import*
from tkinter import ttk,font,messagebox
import socket
import threading
import time
root=Tk()
root.geometry("500x500")
label_font=font.Font(weight="bold",family="times New Roman",size=20)
label=Label(root,text="port number:",font=label_font)
label.place(relx=0.20,rely=0.24)
e1=Entry(root)
e1.place(relx=0.40,rely=0.24,width=150,height=50)
def client():
    s=socket.socket()
    host=socket.gethostname()
    port=12346
    s.connect((host,port))
    s=s.recv(1024)
    print(s.decode()+"I am a client two")
    s.close()
    # thread=threading.Thread(target=client)
    # thread.start()
    # thread.join()

b1=Button(root,text="click",bg="green",font=label_font,command=lambda:client())
b1.place(relx=0.40,rely=0.34)
root.mainloop()
thread=threading.Thread(target=client)
thread.start()
thread.join()

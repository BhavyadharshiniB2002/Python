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
def server():
    s=socket.socket()
    host=socket.gethostname()
    print(host)
    port=12346
    s.bind((host,port))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("got connection from",addr)
        s1='''python is multi pardigm programming language
        development and debugging fast. No compilation process.
        python is a simple and high level language'''
        c.send(s1.encode())
        c.close()
        # thread1=threading.Thread(target=server)
        # thread1.start()
        # thread1.join()
b1=Button(root,text="click",bg="green",font=label_font,command=lambda:server())
b1.place(relx=0.40,rely=0.34)
root.mainloop()
thread1=threading.Thread(target=server)
thread1.start()
thread1.join()
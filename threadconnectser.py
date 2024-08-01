import socket
import threading
import time
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
        s1='''python is an object oriented, interpreted language developed by 
           Guido Van Rossum in 1985-1990 Netherlands. python has a simple syntax and hence
           is easy to understand and learn'''
        c.send(s1.encode())
        c.close()
def server2():
    a=socket.socket()
    host=socket.gethostname()
    print(host)
    port=12347
    a.bind((host,port))
    anext.listen(5)
    while True:
        c,addr=a.accept()
        print("got connection from",addr)
        s1='''python is expressive language and it have large standard
          library and object oriented. it is interpreted. it is platform
          independent and gui programming '''
        c.send(s1.encode())
        c.close()
def client():
    b=socket.socket()
    host=socket.gethostname()
    port=12346
    b.connect((host,port))
    b=b.recv(1024)
    print(b.decode()+"I am a client two")
    b.close()
def client2():
    t=socket.socket()
    host=socket.gethostname()
    port=12347
    t.connect((host,port))
    a=True.recv(1024)
    print(t.decode()+"I am a client two")
    t.close()
thread=threading.Thread(target=server)
thread1=threading.Thread(target=client)
thread2=threading.Thread(target=server2)
thread3=threading.Thread(target=client2)
thread.start()
thread1.start()
thread2.start()
thread3.start()
thread.join()
thread1.join()
thread2.join()
thread3.join()

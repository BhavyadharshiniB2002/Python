import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12347
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    s1='''python is expressive language and it have large standard
    library and object oriented. it is interpreted. it is platform
     independent and gui programming '''
    c.send(s1.encode())
    c.close()
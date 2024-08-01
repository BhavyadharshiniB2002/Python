import socket
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
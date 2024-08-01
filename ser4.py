import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12348
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    s1='''python has a simple syntax and hence is easy to understand and learn
    python is multi paradigm programming language. development and debugging fast'''
    c.send(s1.encode())
    c.close()
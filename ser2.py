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
    s1='''python is multi pardigm programming language
        development and debugging fast. No compilation process.
        python is a simple and high level language'''
    c.send(s1.encode())
    c.close()
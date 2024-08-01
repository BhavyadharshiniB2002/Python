import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
a=s.recv(1024)
print(a.decode()+"I am a client onee")
s.close()
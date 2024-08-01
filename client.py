import socket
s=socket.socket()
host=socket.gethostname()
# port=12345
# s.connect((host,port))
# a=s.recv(1024)
# print(a.decode()+"I am a client one")
# s.close()
def handle_client(c):
    while True:
        data=c.recv(1024)
        if data.decode()=="quit":
            c.close()
        else:
            print("doesnt work)")
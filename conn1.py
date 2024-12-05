import socket
from threading import Thread
host=socket.gethostname()
port=2333
s=socket.socket()
s.connect((host,port));

def recv():
    while True:
        c=s.recv(1024)
        print(c.decode())
def send():
    while True:
    #if c.decode()=="exit":
    #breakpytho
        msg = input("")
        s.send(msg.encode())
t1=Thread(target=send)    
t2=Thread(target=recv)   
t1.start()
t2.start()
   # if (msg=="bye"):
        #break
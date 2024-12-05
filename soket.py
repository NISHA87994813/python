import socket
from threading import Thread
host=socket.gethostname()
port=2333
s=socket.socket()
s.bind((host,port))
s.listen(2)
a,b=s.accept()

print(a)
print(b)
def send():
    while True: 
        msg=input("enter your massage")
        a.send(msg.encode())
def recv():
    while True: 
    #if msg=="byy":
        #break
        msg = a.recv(1024)
        print(msg.decode())
t1=Thread(target=send)    
t2=Thread(target=recv)   
t1.start()
t2.start()
    #if(msg.decode()=="bye"):
       # break
    
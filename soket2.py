import socket
from threading import Thread
host=socket.gethostname()
port=2333
s=socket.socket()
s.bind((host,port))
s.listen(10)
#a,b=s.accept()
#c,d=s.accept()
#e,f=s.accept()
list=[]
def accept():
    while True:
        a,b=s.accept();
        list.append(a);
'''def recv1():
    while True:
        msg=c.recv(1024)
        a.send(msg)
        e.send(msg)
def recv2():
    while True:
        msg=a.recv(1024)
        e.send(msg)
        c.send(msg)
def recv3():
    while True:
        msg=e.recv(1024)
        a.send(msg)
        c.send(msg)
'''
        
def send():
    while True:
        msg=input()
        for i in list:
            i.send(msg.encode())
def recv():
    while True:
        #msg=input()
        for i in list:
            msg=i.recv(1024);
            print(msg.decode())
  

t1=Thread(target=accept)    
t2=Thread(target=send) 
t3=Thread(target=recv)     
t1.start()
t2.start()
t3.start()
    #if(msg.decode()=="bye"):
       # break
    
import threading
from threading import  Thread
import time
def jumping():
    print(threading.current_thread())
    time.sleep(3)
def running():
    print(" i am running")
    print(threading.current_thread())
    
t1=Thread(target=jumping)
t2=Thread(target=running)
t1.start()
t2.start() 
print("i am from main")    
print(threading.current_thread())

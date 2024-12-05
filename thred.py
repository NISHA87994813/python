from threading import Thread
import time
def jumping():
    print(" i am jumping")
def running():
    print(" i am running")
    t1=Thread(target=jumping)
    t1.start()
    #time.sleep(5)

t2=Thread(target=running)
t2.start()
#time.sleep(2)
#running()
#jumping()


#t1=Thread(target=running)
#t2=Thread(target=jumping)
#t1.start()
#t2.start()


  
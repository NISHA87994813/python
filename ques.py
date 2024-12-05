from threading import Thread
def running(name,min):
     print(name,"running")
def jumping(name,min):
     print(name,"jumping")
#t1=Thread(target=running,args=("shakshi",45))
#t2=Thread(target=jumping,args=("nisha",25))  
t1=Thread(target=running,kwargs={"name":"shakshi","min":"45"})
t2=Thread(target=jumping,kwargs={"name":"nisha","min":"25"}) #thred using argument 
t1.start()
t2.start() 
 
class Demo1():
    def demo1(self):
        print("demo1")
    def __init__(self): 
        print("demo1")    
class Demo2(Demo1):
    def demo2(self):
        print("demo2")
    def __init__(self): 
        print("demo2")    
class Demo3(Demo2):
    def demo3(self):
        print("demo3")
    def __init__(self): 
        print("demo3") 
class Demo4(Demo3):
    def demo3(self):
        print("demo3")
    def __init__(self): 
        print("demo3")            
        
d=Demo3()
#d=Demo1()
d.demo1()
d.demo2()
#d.demo3() 
class Demo1():
    def demo1(self):
        print("demo1")
    def __init__(self):
        print("demo1")
        
class Demo2(Demo1):
    def demo2(self):
        print("demo2")
    def __init__(self):
        super().__init__()
        print("demo2")
class Demo3(Demo2):
    def demo2(self):
        print("demo3")
    def __init__(self):
        super().__init__()
        print("demo3")        
        
        
x=Demo3()
x.demo2()
x.demo1()       
    
class Demo1():
    def demo1(self):
        print("demo1")
class Demo2():
    def demo2(self):
        print("demo2")
class Demo3(Demo1,Demo2):
    def demo3(self):
        print("demo3")
        
#d=Demo3()
d=Demo1()
d.demo1()
#d.demo2()
#d.demo3()    
class Emp:
    def setdata(self,name,age,salary):
        self.name=name
        self.age=age      
        self.salary=salary 
    def display(self):
        print(self.name)
        print(self.age)        
        print(self.salary)
e1=Emp()
e1.setdata("nisga",20,30000)
e1.display()


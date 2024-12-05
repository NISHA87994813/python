class Emp:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def __str__(self):
        self.name=name
        self.age=age
        self.sal=sal
        return""
emp=[]
while True:
            print("1.add")
            print("2.update")
            print("3.remove")
            print("4.display")            
            print("5.exit")
            ch=int(input("enter your choice"))
            if ch==1:
                print("1.add")   
                name=input("enter name")
                age=input("enter age")
                sal=input("enter sal")
                e1=Emp(name,age,sal)
                emp.append(e1)
                print(emp)
                                                
            elif ch==2:
                print("2.update") 
                
            elif ch==3:
                print("3.remove")
                n=input("enter your remove emp")
                for i in emp:
                    if i.name==n:
                        print("found")
                        e1=Emp(name,age,sal)
                        emp.remove(e1)
                        print(emp)
                        break
                else:
                    print("not found")
            elif ch==4:
                print("4.display") 
                for i in emp:
                    print(i)
            elif ch==5:
                print("5.exit")
                break
            else:
                print("invalid")
            
            
            
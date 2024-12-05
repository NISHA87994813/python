all_item=[]
def student(student_id,name,age,major):
            #print("student_id",student_id)
            #print("name=",name)
            #print("age=",age)
            #print("major=",major)
            student = (student_id,name,age,major)
            #a=(tuple(student))
            all_item.append(student)

def display():
           print(all_item)
           print(" ")
def delete(student_id):  
            for i in all_item:
                if i[0]==student_id:
                    all_item.pop(student_id)
                    print(all_item)
                    break
            else:
                print("not found")



            

def update(student_id):
    for i in all_item:
    
        if i[0]==student_id:
            newname=input("enter the name")
            newage=input("enter the age")            
            newgander=input("enter the gander")
            m=(student_id,newname,newage,newgander)
            all_item[student_id]=m
            print(m)
        
        
student(0,"nisha",23,"female") 
student(1,"disha",21,"female") 
student(2,"deepa",22,"female") 
student(3,"raj",20,"male") 
display() 
update(2) 
delete(3)        

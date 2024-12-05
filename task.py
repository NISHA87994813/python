list=[3,5,6,8,9,12,4,56,86,98]
while True:
    print("1.add value")
    print("2.remove value")
    print("3.update value")
    print("4.display value")
    print("0.exit")
    ch=int(input("enter your choice"))
    if ch==1:
            print("1.add value")
            value=int(input("enter value"))
            list.append(value)
            print(list)
    elif ch==2:
            print("2.remove value")
            value=int(input("enter value"))
            if value in list:
                    list.remove(value)
                    print(list)
            else:
                    print("not found")
                    
    elif ch==3:        
            print("3.update value")
            old=int(input("enter value"))
            new=int(input("enter value"))
            if old in list:
                    ind=list.index(old)
                    list[ind]=new
                    print(list)
            else:
                     print("not found") 
                     break;
    elif ch==4:
             print("display value")  
             print(list)
    elif ch==0:
             print("exit value")  
             print(list)
             break;
    else:
             print("not found")       
    
    
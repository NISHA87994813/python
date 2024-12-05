x=[6,7,45,76,75,70,87,65,9,23]

print(" 1.add ")
print(" 2.remove ")
print(" 3.update ")
print(" 4.display ")
print(" 0.exit")
ch=int(input("enter the choice"))
    if ch==1:
        print(" 1.add ")
    value=int(input("add value"))
    x.append(vlaue)
    print(x)
    elif ch==2:
        print(" 1.remove ")
        value=int(input("remove value"))
            if value in x:
            x.remove(vlaue)
            print(x)
            else:
            print("not found")
    elif ch==3:
        print(" 3.update ")
        old=int(input("enter value"))
        new=int(input("enter value"))
            if old in x:
                        ind=x.index(old)
                        x[ind]=new
                        print(x)
            else:
                         print("not found") 
                         break;
    elif ch==4:
                 print("display value")  
                 print(x)
    elif ch==0:
                 print("exit value")  
                 print(x)
                 break;
    else:
                 print("not found")       
        


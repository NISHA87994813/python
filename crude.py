list=[1,2,3,4,5,6]
while True:
    print("1.add values")
    print("2.remove values")
    print("3.update values")
    print("4.display values")
    print("0.exit")
    ch=int(input("enter the choice"))
    if ch==1:
            print("1.add values")
            values=int((input("enter the values")))
            list.append(values);
            print(list)
    elif ch==2:
            print("2.remove values")
            values=int((input("enter the values")))
            if values in list:
                list.remove(values);
                print(list)
            else:
                print("not found")
    elif ch==3:
            print("3.update values")
            old=int(input("enter the old values"))
            new=int(input("enter the new  values"))
            if old in list:
                index=list.index(old)
                list[index]=new
            else:
                print("npot found")
                
                
                
    elif ch==4:
            print("4.diplay values")
            print(list)
    elif ch==0:
            print("0.exit")
            break
    else:
            print("not valid")
    
    
    
    
list=[{'email': 'nisha', 'password': '1234'}]
list1=[{'email': 'nisha', 'password': '1234'}]
Questions=[{'Question': 'who', 'ops': ['i', 'y', 'u', 'o'], 'rop': 'i'}]
while True:
    print("1. Teacher")
    print("2. student")
    print("3. exit")
    ch=int(input("enter your choice"))
    if ch==1:
        while True:
            print("1.Teacher")
            print("1.register")
            print("2.login")
            print("0.exit")
            ch=int(input("enter your choice"))
            if ch==1:
                print("1.register")
                d={}
                userName=input("enter your user name")
                password=input("password") 
                d["email"]=userName
                d["password"]=password
                print("successful register")
                list.append(d)
                print(list)
            elif ch==2:
                print("2.login")
                userNameL=input("enter your user name")
                passwordL=input("password")
                for i in list:
                    if i["email"]==userNameL and i["password"]==passwordL:
                        print("login done")
                       
                        while True:
                            
                            print("1. add quetion")
                            print("2. remove")
                            print("3. update")
                            print("4. display")
                            print("5. exit")
                            ch=int(input("enter your choice"))
                            if  ch==1:
                                    print("1. add quetion")
                                    d={}
                                    Q=input("enter your question")
                                    op1=input("enter op1")
                                    op2=input("enter op2")
                                    op3=input("enter op3")
                                    op4=input("enter op4")
                                    rop=input("right option")
                                    d["Question"]=Q
                                    d["ops"]=[op1,op2,op3,op4]
                                    d["rop"]=rop;
                                    Questions.append(d)
                                    print(Questions)
                            elif ch==2: 
                                    Q=input("enter your remove question")
                                    d={}
                                    c=0
                                    for i in Questions:
                                        if i["Question"]==Q:
                                            print("found")
                                            print("2. remove")
                                            Questions.pop(c)
                                            break
                                        c=c+1
                                    else:
                                        print("not found")
                                        
                                        
                                    
                                    
                            elif ch==3:
                                    print("3. update")
                                    Q=input("enter your update question")
                                    d={}
                                    c=0
                                    for i in Questions:
                                        if i["Question"]==Q:
                                            print("found")
                                            Q=input("enter your update question")
                                            op1=input("enter op1")
                                            op2=input("enter op2")
                                            op3=input("enter op3")
                                            op4=input("enter op4")
                                            rop=input("right option")
                                            d["Question"]=Q
                                            d["ops"]=[op1,op2,op3,op4]
                                            d["rop"]=rop;
                                            
                                            Questions[c]=d
                                            print(Questions)
                                            break
                                        c=c+1
                                    else:
                                        print("not found")
                                        
                                    d["ops"]=[op1,op2,op3,op4]
                                    d["rop"]=rop;
                            elif ch==4:
                                    print("4. display")
                            elif ch==5:  
                                    print("5. exit") 
                                    break                                                
                            else:
                                    print("not found")
                                    
                                
                                
                        break
                else:
                    print("not valid")
            elif ch==0:
                   print("0.exit")
                   break               
            else:
                print("not found")
          
    elif ch==2:
        while True:
            print("2.student")
            print("1.register")
            print("2.login")
            print("0.exit")
            
            ch=int(input("enter your choice"))
            if ch==1:
                print("1.register")
                d={}
                userName=input("enter your user name")
                password=input("password") 
                d["email"]=userName
                d["password"]=password
                print("successful register")
                list1.append(d)
                print(list1)
            elif ch==2:
                print("2.login")
                userNameL=input("enter your user name")
                passwordL=input("password")
                for i in list1:
                    if i["email"]==userNameL and i["password"]==passwordL:
                        print("login done")
                        result =0
                        for i in Questions:
                            print(i["Question"])
                            z = i["ops"]
                            print(z[0])
                            print(z[1])
                            print(z[2])
                            print(z[3])
                            ans = input("choose your right op")
                            if ans==i["rop"]:
                                result = result+1
                        print("you total score is = ",result,"/",len(Questions))
                            
                        break
                else:
                    print("not found")
            elif ch==0:
                   print("0.exit")
                   break
                   
            else:
                print("not found")
    elif ch==3:
        print("3.exit")
        break
        
    else:
        print("not found")
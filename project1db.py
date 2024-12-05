import mysql.connector as mc
c = mc.connect(host="localhost",user="root",password="root",database="python")
x = c.cursor()

while True:
    print("1. Teacher")
    print("2. student")
    print("3. exit")
    ch=int(input("enter your choice"))
    if ch==1:
        while True:
            print("1.Teacher ka section ")
            print("1.register")
            print("2.login")
            print("0.exit")
            ch=int(input("enter your choice"))
            if ch==1:
                print("1.register")
                email=input(" ")
                password=input(" ") 
                Q="insert into teacher(user_name,password) values('"+email+"','"+password+"')"
                x.execute(Q)
                c.commit();
                print("register successfully...!")
            elif ch==2:
                email=input("Enter Existing Email")
                password=input("Enter Existing password") 
                #Q="insert into teacher(user_name,password) values('"+email+"','"+password+"')"
                Q="select * from teacher where user_name='"+email+"' and password='"+password+"'"
                x.execute(Q)
                z = x.fetchall()
                if z:
                    print("login successfully..!")
                    while True:
                        print("1. add quetion")
                        print("2. remove")
                        print("3. update")
                        print("4. display")
                        print("5. exit")
                        a=int(input(" enter choice"))
                        if a==1:
                            print("1. add quetion")
                            question=input("enter your question")
                            op1=input("enter op1")
                            op2=input("enter op2")
                            op3=input("enter op3")
                            op4=input("enter op4")
                            rop=input("right option")
                            if rop == op1 or rop==op2 or rop ==op3 or rop ==op4:
                                print("")
                                Q = "insert into questiones1(question,op1,op2,op3,op4,rop) values('"+question+"','"+op1+"','"+op2+"','"+op3+"','"+op4+"','"+rop+"');"
                                x.execute(Q)
                                print("Que added")
                                c.commit()
                            else:
                                print("not possiable")
                        elif a == 2:
                            rem = input()
                            Q="select * from questiones1 where question='"+rem+"'"
                            x.execute(Q)
                            m = x.fetchall()
                            if len(m)>0:
                            
                                Q="delete from questiones1 where question='"+rem+"'";
                                x.execute(Q)
                                c.commit()
                                print("deleted successfully...!")
                            else:
                                print("not found")
                        elif a==3:
                            update= input()
                            Q="select * from questiones1 where question='"+update+"'"
                            x.execute(Q)
                            n = x.fetchall()
                            if len(n)>0:
                                ques=input("enter your question")
                                op1=input("enter op1")
                                op2=input("enter op2")
                                op3=input("enter op3")
                                op4=input("enter op4")
                                rop=input("right option")

                                Q="UPDATE questiones1 SET question='"+ques+"',op1='"+op1+"',op2='"+op2+"',op3='"+op3+"',op4='"+op4+"',rop='"+rop+"' WHERE question='"+update+"'";
                                x.execute(Q)
                                c.commit()
                        elif a==4:
                            print("display")
                            Q="select * from questiones1"
                            x.execute(Q)
                            z = x.fetchall()
                            if z:
                                for i in z:
                                    print("Question ",i[0])
                                    print("Op1 ",i[1])
                                    print("Op2 ",i[2]) 
                                    print("Op3 ",i[3])
                                    print("Op4 ",i[4])  
                                    print("-----------------------------")
                                    
                            else:    
                                    print("nathi registerkaryu...! ja register kar")                                    
                                    
                                    

                        elif a==5:
                            print("exit")
                            break
                        else:
                            print("not valid")
                    
    elif ch==3:
            print("exit")
            break
          
    elif ch==2:
        print("student")
        while True:
            print("1.register")
            print("2.login")
            print("0.exit")
            ch=int(input("enter"))

            if ch==1:
                print("register")
                email=input(" enter email")
                password=input("password ") 
                Q="insert into student(user_name,password) values('"+email+"','"+password+"')"
                x.execute(Q)
                c.commit();
                print("register successfully...!")            
                
            elif ch==2:
                print("login")
                email=input("Enter Existing Email")
                password=input("Enter Existing password") 
                #Q="insert into student(user_name,password) values('"+email+"','"+password+"');"
                Q="select * from student where user_name='"+email+"' and password='"+password+"'"
                x.execute(Q)
                z = x.fetchall()
                if z:
                    print("login successfully..!")
                    Q = "select * from questiones1"
                    x.execute(Q)
                    z = x.fetchall()
                    result=0
                    for i in z:
          
          print("Question ",i[0])
                        print("Op1 ",i[1])
                        print("Op2 ",i[2]) 
                        print("Op3 ",i[3])
                        print("Op4 ",i[4])   
                                             
                        print("-----------------------------")
                        rop= input("choose your right op ")

                       # Q = "insert into questiones1(question,op1,op2,op3,op4,rop) values('"+question+"','"+op1+"','"+op2+"','"+op3+"','"+op4+"','"+rop+"');"                        
                        if rop==i[5]:
                                result = result+1
                    print("you total score is = ",result,"/",len(z))
                            
                    break
                else:
                    print("not found")                    
            elif ch==0:
                print("exit")
                break
            else:
                print("invalid")
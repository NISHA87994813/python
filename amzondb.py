import mysql.connector as mc
c = mc.connect(host="localhost",user="root",password="root",database="python")
x = c.cursor()
while True:
        print("1.seller")
        print("2.buyer")
        print("3.exit")
        ch=int(input("enter your choice"))
        if ch==1:
            print("1.seller") 
            while True:
                
                print("1.register")
                print("2.login")
                print("0.exit")
                ch=int(input("enter your choice"))
                if ch==1:
                        print("1.register")
                        
                        email=input("enter your user name")
                        password=input("password") 
                        Q="insert into seller(user_name,password) values('"+email+"','"+password+"')"
                        x.execute(Q)
                        c.commit();
                        print("register successfully...!")                        
                        
                elif ch==2:
                        print("2.login")
                        email=input("enter your user name")
                        password=input("password")
                        Q="select * from seller where user_name='"+email+"' and password='"+password+"'"
                        x.execute(Q)
                        z = x.fetchall()
                        if z:
                            print("login successfully..!")
                            while True:
                                    print("1.add product")
                                    print("2.remove product")
                                    print("3.update product")
                                    print("4.display product")
                                    print("5.exit")
                                    ch=int(input("enter your choice"))
                                    if ch==1:
                                            print("1.add product")
                                            
                                      
                                            pname=input("enter product name")
                                            pprice=int(input("enter product price"))
                                            pcategory=input("enter product catgary")
                                            pquelity=int(input("enter product quality"))   
                                            
                                          
                                            Q = "insert into products(pname,pprice,pcategory,pquelity) values('"+pname+"','"+str(pprice)+"','"+pcategory+"','"+str(pquelity)+"');"
                                            x.execute(Q)
                                            print("Product added")
                                            c.commit()
                                    elif ch==2:
                                            rem = input("enter pname")
                                            Q="select * from products where pname='"+rem+"'"
                                            x.execute(Q)
                                            m = x.fetchall()
                                            if len(m)>0:
                                            
                                                Q="delete from products where pname='"+rem+"'";
                                                x.execute(Q)
                                                c.commit()
                                                print("deleted successfully...!")
                                            else:
                                                print("not found")                                          
                                    elif ch==3:
                                            update= input("enter yourn product")
                                            Q="select * from products where pname='"+update+"'"
                                            x.execute(Q)
                                            n = x.fetchall()
                                            if len(n)>0:
                                                pname=input("enter your product name")
                                                pprice=input("enter  price")
                                                pcategory=input("enter catgary")
                                                pquelity=input("enter quelity")


                                                Q="update products SET pname='"+pname+"',pprice='"+pprice+"',pcategory='"+pcategory+"',pquelity='"+pquelity+"' WHERE pname='"+update+"'";
                                                x.execute(Q)
                                                print("update successfully")
                                                c.commit()      
                                                  
                                    elif ch==4:
                                        Q="select * from  products"
                                        x.execute(Q)
                                        z = x.fetchall()
                                        if z:
                                            for i in z:
                                                print("pname ",i[0])
                                                print("pprice",i[1])
                                                print("pcategory ",i[2]) 
                                                print("pquality ",i[3])
                                                
                                                print("-----------------------------")
                                                
                                        else:    
                                                print("nathi registerkaryu...! ja register kar")                                    
                                    elif ch==5:
                                        print("exit")
                                        break
                                    else:
                                        print("not valid")
                elif ch==0: 
                    print("exit")
                    break
        elif ch==2:
                print("2.buyer") 
                while True:
                    print("1.register")
                    print("2.login")
                    print("3.exit")
                    ch=int(input("enter choice"))
                    if ch==1:
                       print("1.register")         
                       email=input("enter your user name")
                       password=input("password") 
                       Q="insert into buyer(user_name,password) values('"+email+"','"+password+"')"
                       x.execute(Q)
                       c.commit();
                       print("register successfully...!") 
                    elif ch==2:
                        print("2.login")
                        email=input("enter your user name")
                        password=input("password")
                        Q="select * from buyer where user_name='"+email+"' and password='"+password+"'"
                        x.execute(Q)
                        z = x.fetchall()
                        if z:
                            print("login successfully..!")       
                            while True:
                                print("1.Display all product")
                                print("2.Display by price High to Low")
                                print("3.Display by price Low to High")
                                print("4.Display by category")
                                print("5.Show cart")
                                print("6.Support us")
                                print("0.Exit")
                                ch=int(input(" Enter your choice "))
                                if ch==1:
                                    print("1.Display all product")
                                    Q = "select * from products"
                                    x.execute(Q)
                                    z=x.fetchall()
                                    
                                    for i in z:    
                                        print("Name ",i[0])
                                        print("Price",i[1])
                                        print("Category ",i[2]) 
                                        print("Quality ",i[3])
                                        print("---------------------")
                                        print("which product by in which above list")
                                    buy=input("enter product")
                                    for i in z:
                                        if i[0]==buy:
                                            print("found")
                                            print("enter the quelity want to puches")
                                           
                                            quelity=str(input(""))
                                            if int(quelity) <= int(i[3]):

                                                print("purches successfull")
                                                # i[3]=int(i[3])-int((quelity))
                                                
                                                #print(str(i[3]))
                                                print("do you want add product")
                                                cart=input("")
                                                if cart=="yes":
                                                    print("add cart")


                                                    Q = "insert into cart(pname,pprice,pcategory,pquelity) values('"+i[0]+"','"+str(i[1])+"','"+str(i[2])+"','"+quelity+"');"
                                                    x.execute(Q)
                                                    c.commit()
                                                    
                                                    print("Product added")
                                                   
                                                else:
                                                    print("tnakyou")
                                                    break                                                

                                elif ch==2:  
                                        print("2.Display by price High to Low")
                                        Q="select * from products order by pprice Desc"
                                        x.execute(Q)
                                        result = x.fetchall()
                                        if result:
                                            for i in result:
                                                print("Name:",i[0])
                                                print("Price:",i[1])
                                                print("category:",i[2])
                                                print("quelity:",i[3])
                                                print("-----------------------------")
                                        else:
                                            print("------------------- No products to display -----------------------")

                                        
                                        # print(result)
                                elif ch==3:

                                        Q="select * from products order by pprice Asc"
                                        x.execute(Q)
                                        result = x.fetchall()
                                        if result:
                                            for i in result:
                                                print("Name:",i[0])
                                                print("Price:",i[1])
                                                print("category:",i[2])
                                                print("quelity:",i[3])
                                                print("-----------------------------")
                                        else:
                                            print("------------------- No products to display -----------------------")

                                elif ch==4:
                                    print("display by category")
                                    
                                    Q="select pcategory as pcategory from products"
                                    x.execute(Q)
                                    result=x.fetchall()
                                    if result:
                                        for i in result:
                                                
                                         
                                                print("category:",i[0])
                                              
                                                print("-----------------------------")
                                    else:
                                            print("------------------- No products to display -----------------------")
                                    
                                    categoryb=input("")
                                    G = "select * from products where pcategory = '"+categoryb+"'"
                                    x.execute(G)
                                    b = x.fetchall()
                                    if b:
                                        for j in b:
                                        
                                            print("Found")
                                            print("Name:",j[0])
                                            print("Price:",j[1])
                                            print("category:",j[2])
                                            print("quelity:",j[3])
                                            print("-----------------------------")    
                            

                                elif ch==5:
                                        Q="select * from  cart"
                                        x.execute(Q)
                                        z = x.fetchall()
                                        if z:
                                            for i in z:
                                                print("pname ",i[0])
                                                print("pprice",i[1])
                                                print("pcategory ",i[2]) 
                                                print("pquality ",i[3])
                                                
                                                print("-----------------------------")
                                                
                                        else:    
                                                print("nathi registerkaryu...! ja register kar")                                    

                                        
                                   

admin=[]
product=[{'product Name': 'milk', 'product Price': 50, 'product category': 'a', 'product quelity': 50}, {'product Name': 'sugar', 'product Price': 60, 'product category': 'b', 'product quelity': 20}]
buyer=[{'email': 'n', 'password': 'n'}]
purchescart=[]
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
                        d={}
                        u=input("enter your user name")
                        p=input("password") 
                        d["email"]=u
                        d["password"]=p
                        print("successful register")
                        admin.append(d)
                        print(admin)
                        
                        
                elif ch==2:
                        print("2.login")
                        uName=input("enter your user name")
                        password=input("password")
                        for i in admin:
                            if i["email"]==uName and i["password"]==password:
                                  print("login done")
                                  while True:
                                    print("1.add product")
                                    print("2.remove product")
                                    print("3.update product")
                                    print("4.display product")
                                    print("5.exit")
                                    ch=int(input("enter your choice"))
                                    if ch==1:
                                            print("1.add product")
                                            d={}
                                      
                                            pname=input("enter product name")
                                            pprice=int(input("enter product price"))
                                            pcategory=input("enter product catgary")
                                            pquelity=int(input("enter product quelity"))
                                            if pprice>=0 and pquelity>=0:
                                                d["product Name"]=pname;
                                                d["product Price"]=pprice;
                                                d["product category"]=pcategory;
                                                d["product quelity"]=pquelity;
                                                product.append(d)
                                                print(product)
                                            else:
                                                print("enter valid price")
                                    
                                    elif ch==2:
                                        Product=input("2.remove product")
                                        d={}
                                        c=0
                                        for i in product:
                                            if i["product Name"]==Product:
                                                print("found")
                                         
                                                product.pop(c)
                                                print(product)
                                                break
                                            c=c+1
                                        else:
                                            print("not found")
                                        
                                        
                                
                                    elif ch==3:
                                        print("3.update product")
                                        updateProduct=input("enter update product")
                                        d={}
                                        c=0
                                        for i in updateProduct:
                                            if i["Name"]==updateProduct:
                                                print("found")
                                                while True:
                                                    pname=input("enter product name")
                                                    pprice=int(input("enter product price"))
                                                    pcategory=input("enter product catgary")
                                                    pquelity=int(input("enter product quelity"))
                                                    if pprice>=0 and pquelity>=0:
                                                    
                                                        d["product Name"]=pname;
                                                        d["product Price"]=pprice;
                                                        d["product category"]=pcategory;
                                                        d["product quelity"]=pquelity;
                                                        product[c]=d
                                                        print(product)
                                                        break
                                                    else:
                                                        print("please enter valid price")
                                                    break
                                                c=c+1
                                            else:
                                                print("product not found")
                                                
                                                
                                                    
                                    
                                        
                                        
                                
                                    elif ch==4:
                                        print("4.display product")
                                        print(product)
                                    elif ch==5:
                                        print("exit")
                                        break
                                    else:
                                        print("not valid")
                                        
                                        
                                
                elif ch==0:
                            print("exit")
                            break
                            
                else:
                            print("not valid")
                           
        elif ch==2:
                                        print("2.buyer") 
                                        while True:

                                      
                                            print("1.register")
                                            print("2.login")
                                            print("3.exit")
                                            ch=int(input("enter choice"))
                                            if ch==1:
                                               print("1.register")
                                               d={}
                                               u=input("enter your user name")
                                               p=input("password") 
                                               d["email"]=u
                                               d["password"]=p
                                               print("successful register")
                                               buyer.append(d)
                                               print(buyer)
                                            
                                            elif ch==2:
                                               print("2.login")
                                                                       
                                               uName=input("enter your user name")
                                               password=input("password")
                                               for i in buyer:
                                                    if i["email"]==uName and i["password"]==password:
                                                            print("login done")
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
                                                                      for p in product:
                                                                        print("Name:",p["product Name"])
                                                                        print("Price:",p["product Price"])
                                                                        print("category:",p["product category"])
                                                                        print("quelity:",p["product quelity"])
                                                                        print("-----------------------------")
                                                                      print("which product by in which above list")
                                                                      buy=input("")
                                                                      for i in product:
                                                                        if i["product Name"]==buy:
                                                                            print("found")
                                                                            print("enter the quelity want to puches")
                                                                            quelity=int(input(""))
                                                                            if quelity<=p["product quelity"]:
                                                                                print("purches successfull")
                                                                                p["product quelity"]=p["product quelity"]-quelity
                                                                                print(p["product quelity"])
                                                                                print("do you want add product")
                                                                                cart=input("")
                                                                                if cart=="yes":
                                                                                    print("add cart")
                                                                                    purchase= {"Name":i["product Name"],"Price":i["product Price"],"Category":i["product category"],"quelity":i["product quelity"]}
                                                                                    purchescart.append(purchase)
                                                                                    print(purchescart)
                                                                                else:
                                                                                    print("tnakyou")
                                                                                    break
                                                                            else:
                                                                                print("not enouge quelity")
                                                                elif ch==2:
                                                                    print("2.Display by price High to Low")
                                                                    price=[]
                                                                    for i in product:
                                                                        price.append(i["product Price"])
                                                                    price.sort(reverse=True)
                                                                    for i in price:
                                                                        for j in product:
                                                                            if i==j["product Price"]:
                                                                                print("Name:",j["product Name"])
                                                                                print("Price:",j["product Price"])
                                                                                print("category:",j["product category"])
                                                                                print("quelity:",j["product quelity"])
                                                                                print("-----------------------------")
                                                                                
                                                                      
                                                                      
                                                                elif ch==3:
                                                                      print("3.Display by price Low to High")
                                                                      for i in product:
                                                                        price.append(i["product Price"])
                                                                        price.sort()
                                                                      for i in price:
                                                                        for j in product:
                                                                            if i==j["product Price"]:
                                                                                print("Name:",j["product Name"])
                                                                                print("Price:",j["product Price"])
                                                                                print("category:",j["product category"])
                                                                                print("quelity:",j["product quelity"])
                                                                                print("-----------------------------")
                                                                elif ch==4:
                                                                      print("4.Display by category")
                                                                elif ch==5:
                                                                      print("5.Show cart")
                                                                      print(purchescart)
                                                                      
                                                                elif ch==6:
                                                                      print("6.Support us")
                                                                      print("contact number")
                                                                elif ch==0:
                                                                      print("0.Exit")
                                                                      break
                                                                else:
                                                                
                                                                    print("invalid")
                                                            
                                            
                                            elif ch==0:
                                               print("0.exit")
                                               print("are you sure want exit ")
                                               a=input()
                                               if a=="yes":
                                                break
                                               elif a=="no":
                                                continue
                                               else:
                                                print("yes or no")
                                                break
                                            else:
                                                print("invalid choice ")
                                        
        elif ch==0:
                    print("0.exit")

                    break
        else:
                   print("not valid")
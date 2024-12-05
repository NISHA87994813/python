#try:
    #a=int(input("enter"))
    
    #b=int(input("enter"))
    #try:
        #print(a/b)
#except :
        #print("string not run")
#finally:
    #print("most imp")
try:
    a=int(input("enter"))
    b=int(input("enter"))
    if a==5 and b==4:
        raise ValueError
    else:
        print(a,b)
    #try:
        #print(a/b)
except:
       print("string not run") 
#else:
        #print(" not most imp")
       
#except:
        #print("string not run")    
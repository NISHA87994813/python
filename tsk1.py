def msg(star):
        def innerfun(a):
             print("before star")
             star(a)
             print("after  star")
        return innerfun
            
@msg
def star(b):
         for i in range(1,16):
            print("*") 
b=input("values:")            
star(b)            
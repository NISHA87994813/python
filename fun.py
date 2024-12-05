def max(A,B,C):
    if A>B and A>C:
        print(A, "is max")
          
    elif B>C and B>A:
        print(B,"is max")

    elif C>A and C>B:
        print(C,"is max")
    
    
a=int(input("enter the value a"))
b=int(input("enter the value b"))
c=int(input("enter the value c"))
max(a,b,c)
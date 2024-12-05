lst=[1,2,3,4,5,6,7,8,9,10]
y=lambda i:i if i%2==0 else ""
            
x=filter(y,lst)
print(list(x))           
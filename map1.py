lst=[1,2,3,4,5,6,7,8,9,10]
x=lambda i:i if i%3==0 else "none"
            
x=map(x,lst)
print(list(x))           
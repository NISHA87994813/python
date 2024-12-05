def gen():
    yield "hello"
    yield "buy"
x=gen()
print(next(x))    
print(next(x))   
 
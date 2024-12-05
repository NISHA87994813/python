

#a=int(input("enter"))
#z=list(i for i  in range(100)) #compherehsion method
def gen():
    #for i in range (1000):
    return "bye"
    yield "QWERTY"

x = gen()
try:
    print(next(x))
except StopIteration as e:
    print(next(x))


#for i in gen():
    #print(i)
 
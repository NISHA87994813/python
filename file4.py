z = open("file1.txt","r")
a=z.read()
n= open("vowel.txt","w")
b= open("constant.txt","w")

for i in p:
    if i=="a" and i=="e" and i=="i" and i=="o"and i=="u":
        n.write(i)
    else:
        b.write(i)
n.close()
b.close()

z.close()        


a=open("note.txt","r")
b=a.read()
#b=a.write("hello")
a.close()
c=open("file1.txt","w")
c.write(b);


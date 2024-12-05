import pickle
# z=open("file.txt","wb")
# z=open("file.txt","ab")
# pickle.dump("hii python",z)
# pickle.dump("what",z)
# z.close();
z=open("file.txt","rb")
#try:
while True:
    print(pickle.load(z))
#print(pickle.load(z))
#print(pickle.load(z))
#print(pickle.load(z))
#print(pickle.load(z))
#except:
    print("not in file")

z.close();
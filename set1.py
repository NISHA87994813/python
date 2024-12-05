s={1,2,3,4,5,6,7,8,"nisha"}
print(dir(s))
z=dir(s)
for i in z:
    if '__' not in i:
        print(i)
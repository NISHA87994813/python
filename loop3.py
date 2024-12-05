'''for j in range(5):
    for i in range(5):
        print("*",end="");
    print()
    '''
for j in range(5):
    for i in range(5):
        if i==0:
            print("$",end=" ")
        elif i==4:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
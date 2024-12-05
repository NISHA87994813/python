list=[1,2,3,4,5,6,78,3,6,78,1,2,3]
sum=0
for i in list:
    #sum=sum+i
    sum+=i
avg=sum/len(list)
    
print("sum of list:",sum)
print("avg of list:",avg)        
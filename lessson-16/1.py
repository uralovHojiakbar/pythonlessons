num=[9,1,2,9,3,4,5,9]
k=9
indexes=[]
for i in range(len(num)):
    if num[i]==k:
        indexes.append(i)
print(indexes)
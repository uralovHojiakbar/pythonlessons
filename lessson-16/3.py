lst1=[1,1,1,2,2,3]
k=2
lis2=[]
set1=set(lst1)
for i in set1:
    if lst1.count(i)>=k:
        lis2.append(i)
print(lis2)
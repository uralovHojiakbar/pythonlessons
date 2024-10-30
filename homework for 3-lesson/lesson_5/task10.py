lst1=[1,2,3,2,3,4,6]
lst2=[3,5,7,2,6,3,1]
common_e=[]
for x in lst1:
    for y in lst2:
        if x==y and common_e.count(x)==0:
            common_e.append(x)
print(common_e)
list1=[1,3,5]
list2=[2,4,6]
list3=[]
for x in list1:
    list3.append(x)
for x in list2:
    list3.append(x)
list3.sort()
print(list3)
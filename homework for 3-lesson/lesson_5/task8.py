list=[1,2,3,4,5,6,7,8,9]
even_num=[]
odd_num=[]
for x in list:
    if x%2==0:
        even_num.append(x)
    else:
        odd_num.append(x)
print(even_num)
print(odd_num)
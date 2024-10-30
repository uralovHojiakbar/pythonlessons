numb=[1,3,5,7,9,]
sum=0
for i in range(0,len(numb),2):
    if i%2==0:
        sum+=numb[i]
print(f"sum of  elements at even elements = {sum}")

my_list=[1,5,'banana',10,'apple',20]
sum=0
for i in my_list:
    if str(i).isdigit():
        sum+=1
print(sum)
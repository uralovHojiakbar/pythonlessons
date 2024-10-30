# colr=input('enter the color ').lower()
# if colr=='red':
#     print("Stop")
# if colr=='yellow':
#     print('prepare to stop')
# if colr=='green':
#     print('goo')


# disc=int(input('enter the your money '))
# if disc>=100:
#     print('you apply a 10%')
# else:
#     print('apply 5% ')


# customer_ser=int(input('enter cost'))
# quality=input('enter our service ').casefold()
# if quality=='excellent':
#     print(customer_ser-(customer_ser*20)/100)
# elif quality=='good':
#     print(customer_ser-(customer_ser*15)/100)
# elif quality=='average':
#     print(customer_ser-(customer_ser*10)/100)
age = int(input('Enter age: '))
mem_type = input('Enter membership type:').lower()
if age >= 18 and age <= 60:
    if mem_type == 'premium':
        print(' 10% discount')
    else:
        print('There is no discount ')
elif age > 60:
    print('Our seniors you have 15% discount')
elif age <= 18:
    if mem_type == 'basic':
        print('Under age you have 20% discount')
    else:
        print('For under age there is no discoun')





import math
dic = {'math': [4,5,3,4,5,5], 'english': [3,2,4,4,2,3], 'programming': [5,4,5,5,4,4,5,5]}
dic_res = {}
for x,y in zip(dic.keys(), dic.values()):
    dic_res[f'{x} avarage'] = round(sum(y) / len(y))

print(dic_res)
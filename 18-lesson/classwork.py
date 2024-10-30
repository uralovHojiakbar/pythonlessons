# date=(input('enter the date ::'))
# m=int(date[3]+date[4])
# d=int(date[0]+date[1])
# if m==12 or m==1 or m==2:
#     if d%2==0:
#         print('it is  snowing ')
#     else:
#         print('it is not snowing')
# elif m==9 or m==10 or m==11:
#     if d%2==0:
#         print('it is raining')
#     else:
#         print('it is not  raining')
# elif m==6 or m==7 or m==8:
#     if d%2==0:
#         print('it is summer ')
# elif m==3 or m==4 or m==5:
#     if d%2==0:
#         print('it is spring')




phone=input('enter your  phone number ::')
number=0
for i in phone:
    if i.isalpha():
        print('it is wrong  numbeer')
        exit()
else:
    number=int(phone[3]+phone[4])
    if number==93:
        print('it is Ucell')
    elif number==33:
        print('it is Humans')
    elif number==99:
        print('it is Uzmobile')

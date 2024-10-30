# yosh=int(input('enter the age '))
# if yosh<12:
#     print('sizga kirish bepul ')
# elif yosh<18:
#     print("kirish besh ming  sum ")
# else:
#     print('kirish 20.000')\
# age =int(input('enter the age '))
# if age<5:
#     narh=0
# elif age<12:
#     narh=5000
# elif age<18:
#     narh=10000
# else:
#     narh=20000
# print(f"sizga kirish {narh} sum")
# kun=input('enter the day ')
# if kun.lower()=='shanba'or 'yakshanba ':
#     print('bugun dam olish kuni ')
# else:
#     print('bugun ishn kuni ')
# kun=input('bugun kun nima ')
# harorat=int(input('enter the temp'))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print('chumilgani kettik ')
# else:
#     print('bugun dam olamiz ')
# menu=['osh','somsa ','shurva','shashlik']
# buyurtmalar=['osh','kolbasa','non','choy']
# for taom in buyurtmalar:
#     if taom in menu:
#         print('buyurtma bor ')
#     else:
#         print('uzr yuq ekan ')
# ismlar={'ozod':'shamsiyev','age':25,'job':'talaba','course':1}
# for kalit,qiymat in ismlar.items():
#     print(f"kalit {kalit}")
#     print(f"qiymat {qiymat}")
# mevalar={'olma':12000,'shaftoli':10000,'urik':25000,'gilos':10000}
# for kalitlar in mevalar.keys():
#     print(kalitlar.title())
# davlatlar={'davlatlar':'poytaxtlar','ozbekiistan':'toshkent','usa':'washington','Rossiya':'moskva','tojikiston':'dushanbe'}
# nat=input('enter the nation ')
# for i in davlatlar:
#     if nat==i:
#         print(davlatlar[i])
# menu={'osh':10000,'manti':20000,'tabaka':2300,'non':1234,'choy':2323,'assorti':500}
# book1=input('enter your first book')
# book2=input('enter your second food')
# book3=input('enter your third book ')
# for i in menu.items():
#     if book1==i or book2==i or book3==i:
#         print('your book is {i}')
# car0={'model':'gentra',
#     'yil':2019,
#     'narx':13000}
# car1={'model':'nexia3',
#     'yil':2018,
#     'narx':15000}
# car2={'model':'lacetti',
#     'yil':2020,
#     'narx':9000}
# car3=[car0,car1,car2]
# for car in car3:
#     print(f"{car['model'].title()}, "
#         f"{car['yil']}, "
# #         f"{car['narx']}")
# malibus=[]
# for i in range(10):
#     new_car={'model':'malibu',
#             'rang':'none',
#             'yil':2019,
#             'narx':2020,
#             'km':0,
#             'korobka':'avto'}
#     malibus.append(new_car)
# for malibu in malibus[1:7]:
#     malibu['rang']='qizil'
#     # print(malibu)

# print(malibus)
dasturchilar={
    'Ali':['c++','python'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
}
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi tillarni biladi")
    for til in tillar:
        print(til.upper())

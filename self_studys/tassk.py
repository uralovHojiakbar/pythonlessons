# cars={'model':'ferrari','color':'red'}
# print(cars['model'])
# print(cars['color'])
# talaba={'ism':'uralov hojiakbar','yosh':'24','year':'2000'}
# talaba['kurs']=1
# talaba['facultet']='IT'
# talaba['ism']='uralov sardor'
# print(talaba)
# talaba={}
# talaba['ism'] = 'rasul qobilov'
# talaba['yosh']= 20
# talaba['kurs'] = 1
# print(talaba)
# del talaba['yosh']
# print(talaba)
# brother={'age':21,'tyil':2003,'name':'Alisher'}
# print(f"ismi {brother['name']} tugilgan yil {brother['tyil']} yoshi {brother['age']}")
# taomlar={ 'ali':'osh',
#             'vali':'shashlik',
#             'hasan':'somsa',
#             'husan':'lagmon',
#         }
# taom=taomlar['ali']
# print(f"alining sevimli taomi {taom}")
# keys={'integer':'butun son','float':'kasr son','string':'matn'}
# user=input('enter smth of them')
# print(keys[user])
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib unga,
#     salom beruvchi funksiya"""
#     print(f"assalomu alaykum {ism.title()}")
# salom_ber('hasan')
# print(salom_ber.__doc__)
# def ism_familya(ism,familya):
#     """foydalanuvchini ism va familyasini jamlab ,
#     chiqaradigan funksiya"""  
#     print(f"ism {ism.title()}\n"
#         f"familya {familya.title()}")  
# ism_familya('hasan','olimov')
# def yosh_hisoblagich(ism,tyil):
#     """fooydalanuvchi ismini va yoshini kiritadi ,
#     tugilgan yilini hisoblab chiqarib beradi"""
#     print(f"foydalanuvchini ismi {ism.title()}\n"
#         f"foydalanivchinni yoshi{2024-tyil}")
# yosh_hisoblagich('olim',2004)
# def ism_familya(ism, familya):
#     print(f"foydalanuvchi ismi {ism.title()}\n"
#         f"foydalanuvchi familyasi {familya.title()}")
# ism_familya(familya="uralov",ism="sardor")
# def yosh_hisoblagich(tyil, joriy_yil=2024):
#     print(joriy_yil-tyil)
# yosh_hisoblagich(2000)
# def yosh_hisobla(ism, tyli):
#     print(f"{ism.title()} {2024-tyli} yoshda")
# yosh_hisobla('olim',1997)
# def kvadrat_kub(son):
#     print(f"sonning kvadrati {son*son}\n"
#         f"sonning kubi {son*son*son}")
# kvadrat_kub(2)z

# def juft_toq(son):
#     if son%2==0:
#         print('juft son')
#     else:
#         son%2!=0
#         print('toq son')
# juft_toq(12)
# def katta_kichik(son1,son2):
#     if son1>son2:
#         print(f"{son1} katta")
#     elif son1<son2:
#         print(f"{son2} katta")
#     else:
#         print('ikkala son ham teng')
# katta_kichik(12,34)
# def daraja(son, daraja=2):
#     print(pow(son,daraja))
# daraja(5)
def ikkiga_bulinish(son):
    for i in range(2,11):
        if i%son==0:
            print(f"berilgan son {i} ga bulinadi")
ikkiga_bulinish(2)

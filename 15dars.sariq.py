# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:12:48 2021

@author: USER
"""

# 15dars lug`at elementlari
# muallif AQR 17/03/2021//////10:15time

#talaba_0 = {
#    'ism':'ahad',
#    'familiya':'qayum',
#    'yosh': 35,
#    'fakultet':'sanat',
#    'kurs': 4
#    }
#print(talaba_0.items())

#for key, value in talaba_0.items():
 #   print(f"Kalit:{key}")
#    print(f"Qiymat:{value} \n")
    
#telefonlar = {
# 'ali':'iphone',
# 'vali':'galaxy s9',
# 'olim':'mi10 pro',
# 'ahad':'3110',
# }

#for k, q in telefonlar. items():
##    print(f"{k.title()}ning telefoni {q}")


# .keys()
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':80000,
    'shaftoli':60000
      
#print(mahsulotlar.keys())print('Do`kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{bozorlik.title()} {mahsulotlar[mahsulot]}so`m")

#for buyum in bozorlik:
 #   if buyum not in mahsulotlar:
   #      print(f"Iltimos do`koningizga {buyum} ham olib keling")



































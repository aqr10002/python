# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:08:07 2021

@author: Professional
"""

# 35-dars XATOLAR BILAN ISHLASH
# muallif AQR .........13/04/2021...........18:11 tm,,,,,...........

#yosh = input("Yoshingizni kiriting: ")

#try:
#    yosh = int(yosh)
     
#except ValueError:
#    print("Siz butun son kiritmadingiz")
#else:
 #   print(f"Siz {2021-yosh} yilda tug'ilgansiz ")
    
    
#print("Dastur davom etayapti")
#print("Dastur tugadi")

# ZeroDivisionError
#x,y=5,10
#try:
    
#    y/(x-5)
#except ZeroDivisionError:
#    print("o ga bo'lish mumkun emas")

#mevalar = ['olma','anor','anjir','uzum']
#try:
#    print(mevalar[2])
#except IndexError:
 #   print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
    
#user = {"username":"sariqdev",
   #     "status":"admin",
  #      "email":"admin@sariq.dev",
  #      "phone":"998971114777"}

#key="tel"
#try:
#    print(f"Foydalanuvchi: {user[key]}")
#except KeyError:
#    print("Bunday kalit mavjud emas")
    
#print(user['username'])
    
#filename = "data.txt"
#try:
###    with open(filename) as f:
#        text = f.read()
#except FileNotFoundError:
   # print(f"{filename} mavjut emas")

#import json
#files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
#for filename in files:
#    try:
##        with open(filename) as f:
 #           talaba = json.load(f)
#    except FileNotFoundError:
  #      pass
  #      print(f"{filename} mavjut emas")
  #  else:
  #      print(talaba['ism'])
        #fayl ustida turli amallar
#n = input("Butun son kiriting: ")
#try:
#    n = int(n)
#    x=20/n
#except ValueError:
#    print("Butun son kiritmadingiz")
#except ZeroDivisionError:
#    print("0 ga bo'lib bo'lmaydi")
#else:
 #   print(f"x={x}")

while True:
    yosh = input("Yoshingizni kirting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
        
print(f"Siz {2021-yosh} yilda tug'ilgansiz")































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
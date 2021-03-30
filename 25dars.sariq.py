# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:32:52 2021

@author: USER
"""

# 25-dars::::son topish o`yini
# muallif AQR////////////////29/03/2021///////19:35 tm''''''''''''''

import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
    return taxminlar
    print(f"Tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")

def sontop_pc(x=10):
    input(f" 1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonni o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()) 
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men{taxminlar} ta taxmin bilan topdim!")
    return taxminlar
    
def play(x=10):
    while True:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print("Men yudim!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))
    
    
    
    


# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:10:54 2021

@author: USER
"""

# 28-dars   KLASSLAR 
# muallif AQR  ///////31/03/2021.............17:12 tm''''''''''


class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.tyil
    
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya},tug'ilgan yilim {self.tyil}"
        
        
talaba1 = Talaba("Azam","Axrorov",1999)
talaba2 = Talaba("Toir","Zafarov",1998)
talaba3 = Talaba("Sunnat","Karimov",1997)

        
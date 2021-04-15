# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:34:05 2021

@author: Professional
"""

# 37-dars KLASSLARNI TEKSHIRISH
# muallif AQR ...............14/04/2021..........17:37 tm............



class Car:
    """(self,make,model,year,km=0,price=None)"""
    def __init__(self,make,model,year,km=0,price=None):
        self.make = makeimport unittest
from cars import Car
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
        
    def set_price(self,price):
       self.price = price
       
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")
            
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title} "
        info += f"{self.year}-yil, {self.__km}km yurgan"
        if self.price:
            info += f" Narhi: {self.price}"
        return info
    
    def get_km(self):
        return self.__km
    
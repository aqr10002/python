# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:13:26 2021

@author: Professional
"""

# 31-dars INKAPSULATSIYA VA KLASSGA OID XUSUSIYAT VA METODLAR
# muallif AQR
#  09/04/2021///////'''''16:16 tm'''''''''''


from uuid import uuid4
class Avto:
    """Avtomabil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomabilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod    
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            print("Moshina kmkamaytirib bo'lmaydi")
        
avto1 = Avto("GM","Malibu","Qora",2021,44000,1000)
avto2 = Avto("GM","Gentra","Oq",2021,15000,1000)
avto3 = Avto("Toyota","Carolla","Qizil",2021,55000,1000)
print(avto1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
            
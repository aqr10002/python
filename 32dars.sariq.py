# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:17:09 2021

@author: Professional
"""

# 32-dars  DUNDER METODLAR
# muallif AQR
#  09/04/2021''''''''''''''32:21 tm,,,,,,,,,,,,,,,


class Avto:
    __num_avto = 0
    """Avtomabil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomabilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    def __repr__(self):
        return f"Avto: {self.make} {self.model}" 
    
    def __eq__(self,y):
        return self.narh==y.narh
    
    def __lt__(self,y):
        return self.narh<y.narh
    
    def __le__(self,y):
        return self.narh<=y.narh
    
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,nome):
        self.nome = nome
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.nome} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat
        
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
    
    def __add__(self,y):
        if isinstance(y,AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.nome} {y.nome}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y,Avto):
            self.add_avto(y)
            
    
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")
                
                
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2021,44000)
avto2 = Avto("GM","lacetti","Oq",2020,20000)
avto3 = Avto("Toyota","Carolla","Silver",2019,40000)
salon1.add_avto(avto1,avto2,avto3)

avto4 = Avto("Mazda","6","Sariq",2014,37000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,33000)
avto6 = Avto("Honda","Accord","Yashil",2019,43000)
salon2(avto4,avto5,avto6)














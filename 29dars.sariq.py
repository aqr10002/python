# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:07:13 2021

@author: USER
"""

# 29-dars   OBYEKLAR BILAN ISHLASH
# mullif  AQR  ..........31/03/2021''''''''''''18:09 tm........


class Talaba:
    """Talba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def set_bosqich(self,yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
    
    def updata_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_age(self,yil):
        """Talabaning tug'ilgan yilini qaytaradi"""
        return yil - self.tyil
    
class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
          self.nomi = nomi
          self.talabalar_soni = 0
          self.talabalar = []
            
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilagan talabalar haqida ma'lumot"""
        talabalar = []
        for talaba in self.talabalar:
            talabalar.append(talaba.get.fullname())
        return talabalar
       # return [talaba.get_fullname() for talaba in self.talabalar]
    
def see_medhods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]



matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Azam","Axrorov",1999)
talaba2 = Talaba("Toir","Zafarov",1998)
talaba3 = Talaba("Sunnat","Karimov",1997)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)     

#print(matematika.talabalar_soni)
#


#def tanishtir(self):
 #      return f"Ismim {self.ism} {self.familiya},tug'ilgan yilim {self.tyil}"
        
        
#talaba1 = Talaba("Azam","Axrorov",1999)
#talaba2 = Talaba("Toir","Zafarov",1998)
#talaba3 = Talaba("Sunnat","Karimov",1997)
        
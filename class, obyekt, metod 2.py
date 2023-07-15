# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 14:32:54 2023

@author: Mavlonbek
"""

class Avto:
    """Avtomabillar haqida class"""
    def __init__(self,model,kompaniya,rang,yil,narh):
        self.model=model
        self.kompaniya=kompaniya
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.km=0
    def get_model(self):
        """ Avtomabil modelini qayaradigan metod """
        return self.model
    
    def get_kompaniya(self):
        """ Avtomabol kompaniyasini qaytaruvchi metod """
        return self.kompaniya
    
    def get_rang(self):
        """ Avtomabil rangini qaytaruvchi metod """
        return self.rang
    
    def get_yil(self):
        """ Avtomabilning ishlab chiqarilgan yilini qaytarvchi metod """
        return self.yil
    
    def get_narh(self):
        """ Avtomabil narhini qaytaruvchi metod """
        return self.narh
    
    def set_km(self,km):
        """ Avtomabil yurgan km ni o'zgartiruvchi metod"""
        self.km=km
        
    def get_info(self):
        """ Avtomabil haqidagi to'liq malumotlarni qaytaradi """
        return f"{self.rang} {self.model} {self.kompaniya} tomonidan {self.yil}-yilda ishlab chiqarilgan, Narhi: {self.narh} , {self.km} km yo'l bosgan"


class Avtosalon():
    """ Avtomabillarni yig'uvchi avtosalon """
    def __init__(self,salon_nomi):
        self.nom=salon_nomi
        self.son=0
        self.avtomabillar=[]
        
    def get_nom(self):
        return self.nom
    
    def set_avtomabillar(self,avtomabil):
        """ Avtomabil qabul qilib ro'yxatga uzatuvchi metod """
        self.avtomabillar.append(self.avtomabil)
        self.numbers+=1
        
    def get_avto_ruyxat(self):
        return [avto.get_info() for avto in self.avtomabillar]
    
    def get_avto_numbers(self):
        """ Avtomabillar sonini aytaruvchi metod """
        return self.numbers
    
avto1=Avto('Malibu','GM','Qora',2022,5000)
avto2=Avto('Mersedes Mybach','Mersedes Benz','Oq',2020,200000)
avto4=Avto('Gentra','GM','Kulrang',2023,20000)
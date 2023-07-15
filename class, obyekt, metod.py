# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:02:00 2023

@author: Mavlonbek
"""

class User:
    def __init__(self,name,user_name,emile,emile_password):
        self.name=name
        self.username=user_name
        self.emile=emile
        self.emilepassword=emile_password
        
    def get_name(self):
        return self.name
    
    def get_username(self):
        return self.username
    
    def get_emile(self):
        return self.emile
    
    def get_geemilepassword(self):
        return self.emilepassword
    
    def get_info(self):
        malumotlar=f"Foydalanuvchi ismi: {(self.name).title()}"
        malumotlar+=f"Foydalanuvchi nomi: {self.username}"
        malumotlar+=f"emile: {self.emile}"
        malumotlar+=f"emile parol: {self.emilepassword}/n"
        return malumotlar
    
foydalanuvchi1=User("mavlon",'developer','toshtemerovmavlon@gmail.com',"JGmji12345")
foydalanuvchi2=User("mavlonbek",'programmer','mavlonbektoshtemirov54@gmail.com',"JGmji12345")
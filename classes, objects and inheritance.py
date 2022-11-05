# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 09:07:28 2021

@author: aln_m
@title: classes, objects and inheritance
"""

class Patient(object):
    status = 'Patient'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.conditions = []
        
    def get_detail(self):
        print(f'Patiend record: {self.name}, {self.age} years \n')
        print(f'Current info: {self.conditions}')
        
class Infant(Patient):
    def __init__(self,name,age):
        self.vaccinations = []
        super().__init__(name, age)
    def add_vac(self, vaccine):
        self.vaccinations.append(vaccine)
        
    def get_details(self):
        print(f'Patiend record: {self.name}, {self.age} years \n')
        print(f'Current info: {self.conditions}')
        print(f'Patient vaccination: {self.vaccinations}')
        
alan = Patient('Alan Martinez', 28)
alan.conditions = 'Good health'
print(alan.name+" "+str(alan.age)+" "+alan.conditions)

ariel = Infant("Ariel Luna", 13)
ariel.conditions = 'Buena salud'
ariel.add_vac("Completo")
print(ariel.get_details())

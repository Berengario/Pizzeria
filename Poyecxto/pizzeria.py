'''
Created on 7 mar. 2018

@author: Eider
'''




class Pizzeria:
    def __init__(self, izena, helbidea, telefonoa):
        self.izena=izena
        self.helbidea=helbidea
        self.telefonoa=telefonoa
class Eskaera:
    def __init__(self):
        print()        
class Edaria(Eskaera):
    def __init__(self):
        print("kaixo")
class Pizza(Eskaera):
    def __init__(self):  
        print("tu")
class Ordaindu:
    def __init__(self):
        print()
class Dirua(Ordaindu):
    def __init__(self):
        print("Milesker timatzeagatik.")
class Txartela(Ordaindu):
    def __init__(self):
        print()


print("Hau testing branch-a probatzeko egin dugu txo!")
'''
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''
import math


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza de {self.raza}')

    def aria(self):
        return math.pi * self.raza ** 2

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return 2 * math.pi * self.raza


c = Cerc(5, 'Rosu')

c.descrie_cerc()
print(f'Aria cecului este de: {c.aria()}')
print(f'Diametrul cecului este de: {c.diametru()}')
print(f'Circumferinta cecului este de: {c.circumferinta()}')




'''
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. 
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. 
Poți verifica schimbarea culorii prin apelarea metodei descrie().
'''

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}')

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare




s = Dreptunghi(12, 10, 'Mov')
s.descrie()

print(f'Aria dreptunghiului este de: {s.aria()}')
print(f'Perimetrul dreptunghiului este de: {s.perimetru()}')

s.schimba_culoarea('Albastru')
s.descrie()

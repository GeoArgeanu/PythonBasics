'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie()
- aceasta printează pe ecran ‘Cel mai probabil am colturi’
'''

from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi.')


# EXEMPLU DE UTILIZAREA
class Dreptunghi(FormaGeometrica):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def aria(self):
        return self.lungime * self.latime


# CREEARE OBIECT DREPTUNGHI
d = Dreptunghi(10, 15)

# APELARE METODELE CLASEI ABSTRACTE
print('-----------------')
print(f'Aria dreptunghiului este: {d.aria()}')
d.descrie()

import math

# class Cerc(FormaGeometrica):
#     def __init__(self, raza):
#         self.raza = raza
#
#     def aria(self):
#         return math.pi * self.raza ** 2
#
#
# c = Cerc(5)
# print('------------------')
# print(f'Aria cercului cu raza {c.raza} este de {c.aria()}')

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
'''


@abstractmethod
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura * 2


# EXEMPLU DE UTILIZARE
p = Patrat(7)
print('-------------------')
print(f'Aria patratului cu latura de {p.latura} este {p.aria()}')
p.descrie()

'''
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă 
ai ales să implementezi metoda abstractă aria)
'''


class Geometrie:
    def __init__(self):
        self._latura = 0  # LATURA ESTE INITIALIZATA CU O VAL IMPLICITA DE 0

    @property
    def latura(self):
        return self._latura

    @latura.setter
    def latura(self, valoare):
        if valoare > 0:
            self._latura = valoare
        else:
            print('Latura tebuie sa fie mai mare de zero.')

    @latura.deleter
    def latura(self):
        print('Stergerea laturii.')
        del self._latura

    def calculare_arie(self):
        # Metoda pt calc ariei formei geometrice
        return self._latura ** 2  # aria patratului


forma = Geometrie()
forma.latura = 5

# getter
print('Latura formei geometrice este: ', forma.latura)

# aria
print('Aria formei geometrice este: ', forma.calculare_arie())

# stergerea laturei
del forma.latura

'''
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul 
folosește field PI mostenit din clasa părinte 
(opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''


# class Cerc(FormaGeometrica):
#     def __init__(self, raza):
#         self._raza = raza
#
#     @property
#     def raza(self):
#         return self._raza
#
#     @raza.setter
#     def raza(self, valoare):
#         if valoare > 0:
#             self._raza = valoare
#         else:
#             print('Raza trebuie sa fie mai mare de 0')
#
#     @raza.deleter
#     def raza(self):
#         print('Stergerea razei')
#         del self._raza
#
#     def calculare_aria(self):
#         return math.pi * (self.raza ** 2)
#
#
# cerc = Cerc(7)
#
#
# print(f'Raza cerculuieste de: {cerc} ')
# print('Aria cercului este de: ', cerc.calculare_aria())

@abstractmethod
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self._raza = raza

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, value):
        if value <= 0:
            raise ValueError("Raza trebuie să fie mai mare decât zero.")
        self._raza = value

    @raza.deleter
    def raza(self):
        del self._raza

    def calcul(self):
        # Presupunând că PI este o proprietate moștenită de la clasa părinte
        return self.PI * self._raza ** 2


# Exemplu de utilizare
cerc = Cerc()
print(f'Raza cercului: {cerc.raza}')
print(f'Aria cercului: {cerc.calcul()}')
cerc.raza = 7
print(f'Raza cercului după modificare: {cerc.raza}')
print(f'Aria cercului după modificare: {cerc.calcul()}')
del cerc.raza
# Încearcă să accesezi raza după ștergere
# print(f'Raza cercului după ștergere: {cerc.raza}')

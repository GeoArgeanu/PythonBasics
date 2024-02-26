'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
   string
   int
   float
   bool
Observație: Valorile vor fi alese de tine după preferințe.
'''

# Variabila de tip string
text = 'Acesta este un sir de caractere'
nume = 'Georgiana'

# Variabila de tip int (integer)
nr_intreg = 42
varsta = 34

# Variabila de tip float
nr_zecimal = 3.90
inaltime = 1.64

# Variabila de tip bool (boolean)
este_adevarat = True
este_fericit = True

'''
3. Utilizează funcția type pentru a verifica 
dacă au tipul de date așteptat.
'''
print('Tipul de date al variabilei este :', type(text))
print('Tipul de date al variabilei este :', type(nume))
print('Tipul de date al variabilei este :', type(nr_intreg))
print('Tipul de date al variabilei este :', type(varsta))
print('Tipul de date al variabilei este :', type(nr_zecimal))
print('Tipul de date al variabilei este :', type(inaltime))
print('Tipul de date al variabilei este :', type(este_adevarat))
print('Tipul de date al variabilei este :', type(este_fericit))

# Definim câteva variabile cu diferite tipuri de date
x = 10  # int
y = 3.90  # float
z = 'Hello'  # str
w = [1, 2, 3]  # lista

# Folosim funcția type pentru a
# obține tipul de date al fiecărei variabile
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(w))  # <class 'list'>

# Folosim funcția isinstance pentru a verifica dacă o
# variabilă are un anumit tip de date
print(isinstance(x, int))  # True
print(isinstance(y, int))  # False
print(isinstance(z, str))  # True
print(isinstance(w, list))  # True
print(isinstance(w, tuple))  # False

'''
4. Rotunjește ‘float’-ul folosind funcția round() și 
salvează această modificare în aceeași variabilă (suprascriere):
Verifică tipul acesteia.
'''
# Rotunjirea valorii și salvarea în aceeași variabilă
nr_zecimal = round(nr_zecimal)  # val cea mai mica

# Verificarea tipului de date
print('Val variabilei dupa rotunjire este: ', nr_zecimal)
print('Tipul de date al variabilei este: ', type(nr_zecimal))

a = 3.141516
a = round(a, 2)  # suprascrie val lui a cu rezultatul rotinjirii
print(a)  # afiseaza 3.14
print(type(a))  # tipul variabilei <class 'float'>

b = 2.78965
b = round(b)  # suprascrie val lui b cu rezultatul rotunjirii
print(b)

c = 3.8976
c = int(c)  # schimba tipul lui b in int
print(c)  # elimina zecimalele => 3

'''
5. Folosește print() și printează în consolă 4 propoziții 
folosind cele 4 variabile. 
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
# functia print() simpla
# print('Acesta este un mesaj')
#
# # fct print() + alte mesaje
# print('Acesta este un' + ' alt mesaj')
#
# #prenume = 'Argeanu'
# print(prenume)
# print('Salut, eu sunt ' + prenume)
#
# age = 34
# print('Eu am ' + str(varsta) + ' ani')

# name = 'Georgiana'
# age = 34
# height = 1.64
# culoare = 'albastru'
# print('Numele meu este ' + name)
# print('Eu am ' + str(age) + ' ani')
# print('Inaltimea mea este de ' + str(height) + ' metri')
# print('Culoarea mea preferata este ' + culoare)

'''
6. Citește de la tastatură:
    numele;
    prenumele.
Afișează: 'Numele complet are x caractere'.
'''
# Citirea numelui și prenumelui de la tastatură
name = input('Introdu numele: ')
name1 = input('Introdu prenumele: ')

# Concatenează numele și prenumele cu un spațiu între ele
nume_complet = name + '' + name1

# Calculează numărul de caractere din numele complet
x = len(nume_complet)
print('Numele cpmlet are ', x, 'caractere')

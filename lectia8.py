'''
1. Scrieţi o funcţie care primeşte ca parametru
lungimea laturii unui pătrat şi returnează aria sa.
'''

# calculeaza aria unui patrat data de lung lat.
# parametrii
# - latura (float sau int): Lungimea lat patratului

# returneaza:
# - Aria patratului (float sau int)

import math


def area_of_the_square(side):
    aria = side ** 2
    return aria


square_side = 5
result = area_of_the_square(square_side)
print(result)

# lungime_latura = float(input('Introdu lung lat patratului: '))
# rezultat = area_of_the_square(lungime_latura)
#
# print(f'Aria patratului cu lat {lungime_latura} este: {rezultat}')


'''
2. Scrieţi un subprogram care primeşte ca parametru 
lungimea laturii unui pătrat şi returnează atât 
lungimea diagonalei, cât şi perimetrul pătratului.
'''


def calc_diagonal_perimeter_square(latura):
    diagonala = latura * math.sqrt(2)
    perimetru = 4 * latura
    return diagonala, perimetru


lungime_latura = 12
rezultate = calc_diagonal_perimeter_square(lungime_latura)
lungime_diagonala, perimetru = rezultate

print('diagonala: ', lungime_diagonala)
print('perimetru: ', perimetru)

'''
3. Scrieţi o funcţie care primeşte ca parametri de intrare 
lungimile celor două catete ale unui triunghi dreptunghic 
şi returnează lungimea ipotenuzei.
'''


def calculeaza_ipotenuza(cateta1, cateta2):
    ipotenuza = math.sqrt(cateta1 ** 2 + cateta2 ** 2)
    return ipotenuza


cateta1 = 5
cateta2 = 6
rezultat = calculeaza_ipotenuza(cateta1, cateta2)
print(rezultat)

'''
4. Scrieţi o funcţie care primeşte 3 parametri de tip real, 
cu semnificaţia de lungimi pentru 3 segmente. 
Funcţia va returna 1 dacă cele trei segmente pot forma un 
triunghi şi 0, în caz contrar.
'''


def verifica_inegalitatea_triung(l1, l2, l3):
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        return 1
    else:
        return 0


lat1 = 5
lat2 = 7
lat3 = 6
rezultat = verifica_inegalitatea_triung(lat1, lat2, lat3)

if rezultat:
    print('Formeaza un triunghi')
else:
    print('NU formeaza un triunghi')

'''
Sa se scrie o functie care citeste de la tastatura un 
text si returneaza toate caracterele folosite in 
acel string ordonate alfabetic.
'''


def caractere_ordonate(text):
    caractere_unice = sorted(set(text))
    return ''.join(caractere_unice)


text_input = input('Introdu un text: ')
rezultat = caractere_ordonate(text_input)
print(f'Caaracterele unice ordonate alfabetic sunt: {rezultat}')


'''
Sa se scrie o functie care primeste ca 
parametri 2 numere si il returneaza pe cel mai mare
'''

def cel_mai_mare(nr1, nr2):
    return max(nr1, nr2)

nr1 = float(input('Introdu primul nr: '))
nr2 = float(input('Introdu al doilea nr: '))
rezultat = cel_mai_mare(nr1, nr2)
print(f'Cel mai mare nr este : {rezultat}')

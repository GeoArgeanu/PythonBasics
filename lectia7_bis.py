'''
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
'''

import random

# numar_secret = random.randint(1, 30)
# numar_ghicit = None
#
# while numar_ghicit != numar_secret:
#     numar_ghicit = int(input('Alege un numar intre 1 si 30: '))
#     if numar_ghicit > numar_secret:
#         print('Numarul secret e mai mic')
#     elif numar_ghicit < numar_secret:
#         print('Numarul secret e mai mare')
#     else:
#         print('Felicitari! Ai ghicit')


'''
14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''

# VARIANTA 1
n = int(input('Introdu un numar: '))
for i in range(1, n + 1):
    print(str(i) * i)

# VARIANTA 2
numar = int(input('Introdu un numar: '))

# Generam piramida
for i in range(1, numar + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()  # adugam o line noua dupa fiecare rand


'''
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

for row in tastatura_telefon:
    for element in row:
        print(f'Cifra curenta este {element}')


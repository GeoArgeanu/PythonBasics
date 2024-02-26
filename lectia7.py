'''
5. Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
5. Modernizează parcul de mașini:
Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in range(len(masini)):
    if masini[i] in ['Trabant', 'Lastun']:
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'

modele_vechi = ', '.join(masini_vechi)
modele_noi = ', '.join(masini)

print(f'Modele vechi: {modele_vechi}')
print(f'Modele noi: {modele_noi}')


'''
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.
'''
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

buget = 25000

# VARIANTA 1 ( UNA SUB ALTA )
print(f'Pentru un buget de sub {buget} euro puteti alege masina:')
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f' - {masina}')


# VARIANTA 2 ( CA SI O LISTA UNA DUPA ALTA)
masini_de_buget = [masina for masina, pret in pret_masini.items() if pret <= buget]
print(f' Sau intr-o lista: {masini_de_buget}')



'''
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nr_3 = 0
# #print('Lista de numere:')
# for numar in numere:
#     #print(numar)
#     if numar == 3:
#         nr_3 += 1
#
# print(f'Nr 3 apare de {nr_3} ori in lista')


'''
8. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea
Calculează și afișează suma numerelor 
(nu ai voie să folosești sum).
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# total = 0
#
# for numar in numere:
#     print(numar)
#     total += numar
#
# print(f'Suma nr din lista este {total}')


'''
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# # Verificăm dacă lista nu este goală
# if not numere:
#     print("Lista este goală.")
# else:
#     cel_mai_mare = numere[0]
#
#     print("Lista de numere:")
#     for numar in numere:
#         print(numar)
#
#         # Verificăm dacă numărul curent este mai mare decât cel mai mare găsit până acum
#         if numar > cel_mai_mare:
#             cel_mai_mare = numar
#
#     print(f"\nCel mai mare număr din listă este: {cel_mai_mare}")


'''
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
'''

print('Lista initiala')
print(numere)

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = - numere[i]

print('Lista dupa inlocuire cu nr negative')
print(numere)


'''
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []


# Verificam dac nr este par sau impar
for numar in alte_numere:

    # Verficam daca e par sau impar
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)

    # Verificam daca nr este poz sau neg
    if numar > 0:
        numere_pozitive.append(numar)
    elif numar < 0:
        numere_negative.append(numar)

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)


'''
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
sorted_numere = sorted(alte_numere)

print('Lista ordonata crescator: ', sorted_numere)

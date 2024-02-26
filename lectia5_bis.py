'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă.
'''

# VARIANTA 1 CU '+'
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista_unificata = lista1 + lista2
# print(lista_unificata)

# VARIANTA 2 CU FCT .extend()
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista1.extend(lista2)
# print(lista1)



'''
4.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Sortează și afișează lista generată.
Sortează numărul 0 folosind o funcție.
Afișaza iar lista.
'''

# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# # Unim cele 2 liste
# lista_unificata = lista1 + lista2
# # Le sortam in ordine crescatoare (.sort())
# lista_unificata.sort()
# print(lista_unificata)
# # Sortam nr 0 in ordine descrescatoare (inversarea listei)
# lista_unificata.sort(reverse=True)
# print(lista_unificata)


'''
5.  Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Folosind un if verifică lista:
Lista este goală.
Lista nu este goală.
'''
lista1 = [3, 1, 0, 2]
lista2 = []

# Verificam lista1 daca e goala
if len(lista1) == 0:
    print('Lista nr.1 este goala')
else:
    print('Lista nr.1 nu este goala')

# Verificam lista1 daca e goala
if len(lista2) == 0:
    print('Lista nr.2 este goala')
else:
    print('Lista nr.2 nu este goala')


'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista1.extend(lista2)
# lista1.clear()
# print(lista1)
# del lista1
# print(lista1)


''''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())
print(dict1.values())


'''
9. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5
Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
for elev, nota in dict1.items():
    print(f'{elev} a luat {nota}')


''''
10. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
 Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
'''
dict1['Dorel'] = 6
print(dict1)


'''
11. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
 Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
'''
# Sterge pe Gigel
if 'Gigel' in dict1:
    del dict1['Gigel']
# Adaugam elev nou
dict1['Ionica'] = 9

# Afisam elevii noi
print('Noii elevi sunt:')
for elev, nota in dict1.items():
    print(f'{elev} - {nota}')


'''
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

# Adaugam 'luni' la zile_sapt
zile_sapt.add('luni')
print(zile_sapt)


'''
14. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')



'''
15. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Afișează diferențele dintre aceste 2 seturi.
'''
diferenta = zile_sapt.difference(weekend)
print(diferenta)


'''
16. Afișează intersecția elementelor din aceste 2 seturi.
'''

intersectia = zile_sapt.intersection(weekend)
print(intersectia)


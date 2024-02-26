'''
7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.
'''
#
# latimea = float(input('Introduceti latimea: '))
# lungimea = float(input('Introduceti lungimea: '))
# aria = lungimea * latimea
# print(f'Aria dreptunghiului este {aria}')


'''
8. Având stringul: 'Coral is either the stupidest animal or 
the smartest rock':
afișează de câte ori apare cuvântul 'the';
'''
# text = 'Coral is either the stupidest animal or the smartest rock'
# cuvant_de_cautat = 'the'
# nr_aparitii = text.count(cuvant_de_cautat)
# print(f'Cuvantul {cuvant_de_cautat} apare de {nr_aparitii} ori in text')



'''
string = 'Coral is either the stupidest animal or the smartest rock'
inlocuieste the cu THE peste tot
# ●	Printează rezultatul.
'''
#text = 'Coral is either the stupidest animal or the smartest rock'
# Varianata cea mai simpla 1
# text_modificat = text.replace('the', 'THE')
# print(text_modificat)

# Varianata 2
# cuvant_de_inlocuit = 'the'
# cuvant_nou = 'THE'
# text_modificat = text.replace(cuvant_de_inlocuit, cuvant_nou)
# print(text_modificat)

'''
10. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
Folosește un assert ca să verifici dacă acest string conține doar numere.
'''
# text = '123456'
# assert text.isnumeric(), 'Textul nu contine doar numere'
# print('Textul contine doar nr')



'''
11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.
'''
# text = input('Introdu un text: ')
# lungime = len(text)
# caracter_mijloc = text[lungime // 2]
# print(f'Caracterul din mijl este {caracter_mijloc}')




'''
12. Folosind o singură linie de cod :
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare.
'''
# text = input('Introdu 2 cuvinte:')
# s1, s2 = text.split()
# print(s1)
# print(s2)



'''
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă 
- indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și 
ultimul caracter => alAbAlA portocAla.
'''
# text = input('Introdu un sir de caractere: ')

# Salvarea primului caractere intr-o variabila
# primul_caracter = text[0]

# # Capitalizarea primului caracter în interiorul șirului
# (cu excepția primului și ultimului caracter)
# text_modificat = primul_caracter + text[1:-1].capitalize() + text[-1]
# print(text_modificat)
# string = input('Introdu un string: ')
# first = string[0]
# interior_modificat = string[1:-1].replace(first, first.upper())
# final_string = string[0] + interior_modificat + string[-1]
# # interiorul string mai putin capetele
# print(final_string)


'''
14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de 
dimensiunea parolei, trebuie să afișeze corect.
'''
# user = input('Introduceti user: ')
# parola = input('Introduceti parola: ')
# stelute = '*' * len(parola)
# print(f'Parola pt user {user} este {stelute} si are {len(parola)} caractere')


'''
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
# x = float(input('Introdu lungimea lat x: '))
# y = float(input('Introdu lungimea lat y: '))
# z = float(input('Introdu lungimea lat z: '))
#
# if x == y == z:
#     print('Triunghiul este echilateral')
# elif x == y or y == z or z == x:
#     print('Triunghiul este isoscel')
# else:
#     print('Triunghiul este oarecare')



'''
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
'''
# litera = input('Introdu o litera: ')
# vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# if litera in vocale:
#     print(f'{litera} este o vocala')
# else:
#     print(f'{litera} este o consoana')



'''
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
# nota = float(input('Introdu nota: '))
#
# if nota > 9:
#     nota_transformata = 'A'
# elif nota > 8:
#     nota_transformata = 'B'
# elif nota > 7:
#     nota_transformata = 'C'
# elif nota > 6:
#     nota_transformata = 'D'
# elif nota > 4:
#     nota_transformata = 'E'
# else:
#     nota_transformata = 'F'
#
# print(f'Nota {nota} corespunde in sistemul specificat cu: {nota_transformata}')



'''
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
# Varianta cea mai simpla
# x = int(input('Introdu un nr intreg: '))
# if x >= 1000:
#     print(f'{x} are cel putin 4 cifre')
# else:
#     print(f'{x} nu are cel putin 4 cifre')


# Varianta nr.2, aflam lung lui x si deducem ca are 4 sau mai multe
# x = int(input('Introdu un nr intreg: '))
# x_str = str(x)  # convertim x in sir de caractere
# x_len = len(x_str)
# print(x_len)

# Varianta cu if
# x = int(input('Introdu un nr. intreg: '))
# x_str = str(x)
# x_len = len(x_str)
#
# if x_len >= 4:
#     print(f'{x} are minim 4 cifre')
# else:
#     print(f'{x} nu are minim 4 cifre')


'''
12.Verifică dacă x are exact 6 cifre
'''
# x = int(input('Introdu un nr. intreg: '))
# x_str = str(x)
#
# if x_str == 6:
#     print(f'{x} are exact 6 cifre')
# else:
#     print(f'{x} nu are exact 6 cifre')


'''
13.Verifică dacă x este număr par sau impar (x e int)
'''
# x = int(input('Introdu un nr: '))
#
# if x % 2 == 0:
#     print(f'{x} este nr. par')
# else:
#     print(f'{x} este nr. impar')


'''
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''
# x = int(input('Introdu primul nr: '))
# y = int(input('Introdu primul nr: '))
# z = int(input('Introdu primul nr: '))

# Varianta nr1
# cel_mai_mare = max(x, y, z)
# print(f'Cel mai mare nr dintre {x}, {y} si {z} este {cel_mai_mare}')

# Variant nr2
# if x > y and x > z:
#     print(f'{x} este nr cel mai mare')
# elif y > z and y > x:
#     print(f'{y} este cel mai mare nr')
# else:
#     print(f'{z} este cel mai mare nr')



'''
15. 
# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
# '''
# X = float(input('Introdu valoare unghiului X: '))
# Y = float(input('Introdu valoare unghiului Y: '))
# Z = float(input('Introdu valoare unghiului Z: '))
#
# if X + Y + Z == 180 and X > 0 and Y > 0 and Z > 0:
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul este invalid')



'''
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
#text = 'Coral is either the stupidest animal or the smartest rock'

# Varianta simpla in care stim textul
# x = int(input('Introdu un nr intreg x: '))
# text_nou = text[:-x]
# print(text_nou)

# Varianta 2 in care nu stim textul
# x = int(input('Introdu un nr intreg x: '))
# if 0 < x < len(text):
#     print(text[:-x])
# else:
#     print('Nr este mai mare decat dim textului')



'''
17. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
 Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
'''
# Varianta 1
# text = 'Coral is either the stupidest animal or the smartest rock'
# text_nou = text[:5] + text[-5:]
# print(text_nou)

# Varianta 2
# text = 'Coral is either the stupidest animal or the smartest rock'
# first = text[:5]
# last = text[-5:]
# new = first + last
# print(new)



'''
18. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Salvează într-o variabilă și afișează indexul de start al cuvântului rock 
(hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' 
'''


# Varianta nr 1
# text = 'Coral is either the stupidest animal or the smartest rock'
# Găsirea indexului de start al cuvântului "rock" folosind metoda find()
# index_rock = text.find('rock')
# Afișarea șirului până la cuvântul "rock"
# text_nou = text[:index_rock]
# print(text_nou)

# Varianta nr. 2
# text = 'Coral is either the stupidest animal or the smartest rock'
# i = text.index('rock')
# print(i)
# print(text[:i])


'''
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''

# import random # importam random
# zar = random.randint(1, 6)
#
# incercare = int(input('Ghiceste nr '))
#
# if incercare < zar:
#     print(f'Ai gresit. Ai ales un nr mai mic. Ai ales {incercare} dar a fost {zar}')
# elif incercare > zar:
#     print(f'Ai gresit. Ai ales un nr mai mare. Ai ales {incercare} dar a fost {zar}')
# else:
#     print('Ai ghicit! Felicitari')



'''
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''
# text = input('Introdu un sir de caractere: ')
#
# # Transformarea șirului la litere mici (lowercase)
# # pentru a ignora sensibilitatea la majuscule/minusculă
# text = text.lower()
#
# # Verificarea dacă primul și ultimul caracter sunt la fel
# assert text[0] == text[-1], 'Primul si ultimul caracter nu sunt la fel'
#
# # Verificarea dacă primul și ultimul caracter sunt la fel
# print('Primul si ultimul caracter sunt la fel')



'''
21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
'''
numere = '0123456789'
# Afișarea numai a numerelor pare
numere_pare = numere[::2] # de la 0 pana la capat si pasul 2
print('Numerele pare:', numere_pare)

# Afișarea numai a numerelor impare
numere_impare = numere[1::2]  # de la 1 pana la capat si pasul 2
print('Numerele impare:', numere_impare)



# avem stringul s
s = '0123456789'

# afisam doar numerele pare
print('Numerele pare sunt:', s[::2])

# afisam doar numerele impare
print('Numerele impare sunt:', s[1::2])













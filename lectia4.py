'''
1. Declară o listă note_muzicale în care să pui
do re mi etc până la do
   Afișeaz-o.
   Inversează ordinea folosind slicing și
suprascrie această listă.
   Printează varianta actuală (inversată).
   Pe această listă aplică o metodă care bănuiești că face
același lucru, adică să îi inverseze ordinea.
   Nu trebuie să o suprascrii în acest caz, deoarece metoda face
asta automat.
   Printează varianta actuală a listei. Practic ai ajuns înapoi
 la varianta inițială.

   Concluzii: slicing e temporar, dacă vrei să păstrezi nouă
variantă va trebui să suprascrii lista sau să o salvezi
într-o listă nouă. Metoda găsită de tine face suprascrierea
automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''

# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print('Lista initiala: ')
# print(note_muzicale)
#
# # Inversează ordinea folosind slicing și suprascrie lista
# note_muzicale = note_muzicale[::-1]
# print('Lista inversata cu slising')
# print(note_muzicale)
#
# # Aplică metoda reverse()
# # pentru a inversa ordinea listei (permanent)
# note_muzicale.reverse()
# print('Lista inversata cu reverse (permanenta)')
# print(note_muzicale)
#
# # Concluzii
# print("Concluzii: slicing e temporar, metoda reverse() face modificarea permanentă.")



'''
2. Declară o listă note_muzicale în care să pui do re mi etc 
până la do
 De câte ori apare ‘do’?
'''
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# aparitii_do = note_muzicale.count('do')
# print(f'do apare de {aparitii_do} ori in lista note_muzicale')



'''
3. Declară o listă note_muzicale în care să pui do re mi etc până la do
Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.
'''
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

# Transforma lista intr-o tupla
tupla_note = tuple(note_muzicale)
print(tupla_note)

# Adaugare de elem noi in tupla mea
tupla_note = tupla_note + ('la',)
print(tupla_note)



'''
4. Declară o listă note_muzicale în care să pui do re mi etc până la do
 Declara un dictionar cu notele muzicale de mai sus. 
 Cheia va fi nota, iar valoarea un numar care arata 
 de cate ori apare nota in gama. Afiseaza-l.
'''
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

# Initializam un dictionar
dictionar_note_muzicale = {}
for nota in note_muzicale:
    if nota in dictionar_note_muzicale:
        dictionar_note_muzicale[nota] += 1
    else:
        dictionar_note_muzicale[nota] = 1

print(dictionar_note_muzicale)




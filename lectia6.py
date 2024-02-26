''''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# VARIANTA CU FOR
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# VARIANTA CU FOR EACH
[print(f'Masina mea preferata este {masina}') for masina in masini]

# WHILE
i = 0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i += 1


'''
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
'''
for i in range(len(masini)):
    if i == 0 or i == len(masini) - 1:
        continue  # Sare peste primul si ultimul elem
    masini[i] = masini[i].upper()
else:
    print(masini)

for i, masina in enumerate(masini):
    if i == 0 or i == len(masini) - 1:
        continue
    masini[i] = masina.upper()
else:
    print(masini)



'''
3.  Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
'''
for masina in masini:
    if masina == 'Opel':
        print('Am găsit mașina dorită de dvs')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')



'''
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
'''

for masina in masini:
    if masina in ['TRABANT', 'LASTUN']:
        continue
    print(f'S-ar putea să vă placă mașina {masina}')



'''
Creeaza urmatoarele variabile: o lista, o tupla, un string.
Itereaza prin fiecare dintre ele, prima data folosind o bucla for,
iar apoi folosind un iterator (ne vom folosi de metodele iter si next):

my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(f’Primul element: {next(my_iterator)}’)
print(fAl doilea element: {next(my_iterator)}’)
print(f’Al treilea element: {next(my_iterator)}’)
print(f’Aici va da eroare: {next(my_iterator)}’)
'''

# Creaza variabilele
# my_list = [1, 2, 3]
# my_tuple = (4, 5, 6)
# my_string = 'Hello World'
#
# print('Iterare prin lista folosind bucla for')
# for item in my_list:
#     print(item)
#
#
# print('\nIterare prin bucla folosind bucla for')  # \n lasa un spatiu intre printuri
# for item in my_tuple:
#     print(item)
#
#
# print('\nIterare prin string folosind o bucla for')
# for char in my_string:
#     print(char)
#
#
# my_iterator = iter(my_tuple)
#
# print(f'\nPrimul element: {next(my_iterator)}')
# print(f'Al doilea element: {next(my_iterator)}')
# print(f'Al treilea element: {next(my_iterator)}')
#
# try:
#     print(f'Aici va aparea o eroare: {next(my_iterator)}')
# except StopIteration:
#     print('Iteratorul a ajuns la final')
#     exit(0)



'''
Declara un string care contine toate literele alfabetului. 
Folosind functia enumerate, care primeste ca si parametru o 
colectie (lista, tupla, string) si returneaza un iterator, 
afiseaza pentru fiecare litera in parte:
`Pe mine ma cheama X si sunt a n-a litera din alfabet`
Nu uite sa gestionezi cazurile speciale (prima litera, etc)
'''

alphabet_string = 'abcdefghijklmnopqrstuvwxyz'

for index, letter in enumerate(alphabet_string, start=1):
    if index == 1:
        print(f'Pe mine ma cheama {letter.upper()} si si sunt prima litera din alfabet.')
    elif index == 26:
        print(f'Pe mine ma cheama {letter.upper()} si si sunt ultima litera din alfabet.')
    else:
        print(f'Pe mine ma cheama {letter.upper()} si sunt a {index}-a litera din alfabet.')



'''
Declara trei liste: una cu oameni, una cu salarii, 
si una cu meserii  (important: trebuie sa aiba 
acelasi numar de elemente). Apoi foloseste functia zip, 
care primeste ca si parametru un numar de colectii si 
returneaza un iterator pentru a afisa:
`Pe mine ma cheama X, sunt de profesie Y, si castig Z ron pe luna`
'''
people = ['Ana', 'Maria', 'George', 'Ionel']
salary = [3500, 4200, 7500, 5600]
jobs = ['Invatatoare', 'Frizer', 'Medic', 'Inginer']

# Verificam ca listele au acelasi nr de elemente
if len(people) == len(salary) == len(jobs):
    # Utilizam functia zip pt a combina listele
    for people, salary, jobs in zip(people, salary, jobs):
        print(f'Pe mine ma cheama {people}, sunt de profesie {jobs} si castig {salary} RON pe luna.')
else:
    print('Listele nu au acelasi numar de elemente')

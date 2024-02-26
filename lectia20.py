'''
Singleton
Se da următoarea clasa:

class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte
din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind
DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima
apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent
'''

class PresedinteRomania:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __str__(self):
        return 'Eu sunt presedintele Romaniei'

    def say_hello(self):
        return f'Salut {self}'


# Testam Singleton
a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')  # Acesta va returna True

# Verificam daca si pentru metoda say_hello
print(a.say_hello())
print(b.say_hello())



'''
Folosim https://jsonplaceholder.typicode.com/guide/
Toate requesturile se vor face prima data in Postman
(pentru verificare), iar apoi folosind libraria requests din Python.

Structura datelor este următoarea:
- fiecare post este deținut de un user, și poate avea mai multe comments
- fiecare album este deținut de un user, și poate avea mai multe photos
- fiecare todo este detinut de un user.

1. Alege un user din lista de useri predefiniti.
Pentru acesta, fa requesturile necesare pentru a afișa următoarele informații:
	-> lista de albume
	-> lista de todos
Pentru a menține output-ul la un nivel acceptabil,
afișează la fiecare dintre aceste liste doar informații
despre primele 3 obiecte, iar apoi afiseaza "+x more albums/todos",
unde x este numărul de obiecte rămase.
'''

import requests
from pprint import pprint


class PostAPIClient:
    URL = 'https://jsonplaceholder.typicode.com'

    def get_user_info(self, userId):
        response = requests.get(f'{self.URL}/posts?userId= {userId}')
        posts = response.json()


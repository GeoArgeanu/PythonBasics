'''
Problema: Gestiunea unei Clase de Elevi
Doriți să dezvoltați un sistem de gestionare a unei clase de elevi
pentru a monitoriza informații precum nume, note, absențe și alte
detalii relevante. Implementați o bază de date care să permită adăugarea,
afișarea, actualizarea și ștergerea datelor despre elevi și să faciliteze
monitorizarea performanței academice.

Cerințe:

Crearea Bazei de Date:
Definiți structura unei baze de date care să includă cel puțin o tabelă
pentru informațiile despre elevi. Decideți coloanele și tipurile de date
potrivite pentru a stoca numele, notele, absențele și alte detalii relevante.

Adăugarea Elevilor:
Implementați funcții pentru adăugarea unui nou elev în baza de date,
oferind posibilitatea de a introduce numele, notele și absențele.

Afișarea Listei de Elevi:
Creați funcții pentru afișarea listei complete a elevilor,
inclusiv detaliile individuale ale fiecărui elev.

Actualizarea Performanței Elevilor:
Implementați funcții pentru actualizarea notele și absențele unui
elev specificat. Asigurați-vă că aceste funcții actualizează datele
corespunzător în baza de date.

Ștergerea unui Elev:
Creați o funcție care permite ștergerea unui elev din baza de date.

Raportare Performanță Clasă:
Dezvoltați o funcție care să ofere o privire de ansamblu asupra
performanței întregii clase, inclusiv media notelor, absențele medii
și orice alte informații relevante.

Opțional: Filtrare și Raportare Personalizată:
Adăugați funcționalități opționale pentru filtrarea și raportarea
personalizată a datelor, permițând utilizatorilor să obțină
informații specifice, cum ar fi elevii cu note peste o anumită valoare
sau absențele într-un interval specific.
id INTEGER PRIMARY KEY AUTOINCREMENT,
        nume TEXT NOT NULL,
        note REAL DEFAULT 0,
        absente INTEGER DEFAULT 0
'''

import sqlite3

# Conectarea la baza de date
conn = sqlite3.connect('Clasa_elevi.db')
cursor = conn.cursor()

# crearea bazei de date
script = '''
CREATE TABLE elevi14 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nume TEXT NOT NULL,
note REAL DEFAULT 0,
absente INTEGER DEFAULT 0);
'''
cursor.execute(script)
studenti = [
    ('Andreea Popa', 8.9, 2),
    ('Marius Apostol', 6.9, 5),
    ('Maria Tudose', 7.9, 3),
    ('Ion Vasile', 9, 5),
    ('Stefan Marin', 8.9, 3),
]

# Adaugare elevi
def adauga_elev(nume, note, absente):
    cursor.execute('INSERT INTO elevi14(nume, note, absente) VALUES(?, ?, ?)', [nume, note, absente])
    conn.commit()
    print('Elev adaugat cu succes')


adauga_elev('Ion Ionut', 9.8, 2)
adauga_elev('Maria Tanase', 7.8, 3)
adauga_elev('Florin Airinei', 10, 0)
adauga_elev('Ana Tudose', 8.6, 4)

# Afisarea listei de elevi
def afiseaza_elevi():
    cursor.execute('SELECT * FROM elevi14')
    return cursor.fetchall()

# Actualizarea performantei elevilor
def actualizeaza_elevi(id, note, absente):
    cursor.execute('UPDATE elevi14 SET note = ?, absente = ? WHERE id = ?', [id, note, absente])
    conn.commit()
actualizeaza_elevi(1, 10, 0)

# Stergera unui elev
def sterge_elev(id):
    cursor.execute('DELETE FROM elevi14 WHERE id = ?', (id,))
    conn.commit()
    print('Elev sters cu succes')

sterge_elev(2)

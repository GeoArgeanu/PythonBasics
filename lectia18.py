'''
Problema: Gestiunea unei Clase de Elevi
Doriți să dezvoltați un sistem de gestionare a unei clase de elevi pentru a
monitoriza informații precum nume, note, absențe și alte detalii relevante.
Implementați o bază de date care să permită adăugarea, afișarea, actualizarea
și ștergerea datelor despre elevi și să faciliteze monitorizarea performanței academice.

Cerințe:

Crearea Bazei de Date:
Definiți structura unei baze de date care să includă cel puțin o tabelă pentru
informațiile despre elevi. Decideți coloanele și tipurile de date potrivite
pentru a stoca numele, notele, absențele și alte detalii relevante.

Adăugarea Elevilor:
Implementați funcții pentru adăugarea unui nou elev în baza de date, oferind
posibilitatea de a introduce numele, notele și absențele.

Afișarea Listei de Elevi:
Creați funcții pentru afișarea listei complete a elevilor, inclusiv detaliile
individuale ale fiecărui elev.

Actualizarea Performanței Elevilor:
Implementați funcții pentru actualizarea notele și absențele unui elev specificat.
Asigurați-vă că aceste funcții actualizează datele corespunzător în baza de date.

Ștergerea unui Elev:
Creați o funcție care permite ștergerea unui elev din baza de date.

Raportare Performanță Clasă:
Dezvoltați o funcție care să ofere o privire de ansamblu asupra performanței
întregii clase, inclusiv media notelor, absențele medii și orice alte informații relevante.

Opțional: Filtrare și Raportare Personalizată:
Adăugați funcționalități opționale pentru filtrarea și raportarea personalizată
a datelor, permițând utilizatorilor să obțină informații specifice, cum ar fi elevii
cu note peste o anumită valoare sau absențele într-un interval specific.
'''
from pprint import pprint

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crearea unei baze de date
engine = create_engine('sqlite:///elevi', echo=True)
Base = declarative_base()


# Definirea modelului pentru tabelul Elevi
class Elev(Base):
    __tablename__ = 'elevi'

    id = Column(Integer, primary_key=True)
    nume = Column(String)
    note = Column(String)  # vom stoca ntele in forma de sir (ex: 9,10,8)
    absente = Column(Integer)

# Crearea tablei in baza de date
Base.metadata.create_all(engine)

# Functii pentru gestionarea elevilor
def adauga_elev(nume, note, absente):
    session = sessionmaker(bind=engine)()
    elev_nou = Elev(nume=nume, note=note, absente=absente)
    session.add(elev_nou)
    session.commit()
    session.close()

def afiseaza_lista_elevi():
    session = sessionmaker(bind=engine)()
    elevi = session.query(Elev).all()
    for elev in elevi:
        print(f'ID: {elev.id}, Nume: {elev.nume}, Note: {elev.note}, Absente: {elev.absente}')
        session.close()

def actualizeaza_performanta_elev(elev_id, note_noi, absente_noi):
    session = sessionmaker(bind=engine)()
    elev = session.query(Elev).filter_by(id=elev_id).first()
    elev.note = note_noi
    elev.absente = absente_noi
    session.commit()
    session.close()

def sterge_elev(elev_id):
    session = sessionmaker(bind=engine)()
    elev = session.query(Elev).filter_by(id=elev_id).first()
    session.delete(elev)
    session.commit()
    session.close()

def raportare_performanta_clasa():
    session = sessionmaker(bind=engine)()
    elevi = session.query(Elev).all()

    medie_note = sum([int(elev.note.split(',')[0]) for elev in elevi])
    medie_absente = sum([elev.absente for elev in elevi]) / len(elevi)

    pprint(f'Medie Note Clasa: {medie_note}')
    pprint(f'Medie Absente Clasa: {medie_absente}')


# Exemplu de utilizare
adauga_elev('Ana', '9, 8, 10', 2)
adauga_elev('Bogdan', '8, 7, 6', 1)

afiseaza_lista_elevi()
actualizeaza_performanta_elev(1, '10, 10, 9', 0)
afiseaza_lista_elevi()
sterge_elev(2)
afiseaza_lista_elevi()
raportare_performanta_clasa()

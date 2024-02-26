'''
1. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return f'Angajat: {self.nume} {self.prenume} Salariu: {self.salariu}'

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu += self.salariu * (procent / 100)


angajat1 = Angajat('Geo', 'Argeanu', 4000)
print(angajat1.descrie())
print(f'Nume complet {angajat1.nume_complet()}')
print(f'Salariu lunar {angajat1.salariu_lunar()}')
print(f'Salariu anual {angajat1.salariu_anual()}')


angajat1.marire_salariu(10)
print(f'Salariu după mărire: {angajat1.salariu}')


'''
 2. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, 
toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total 
Telefon |      7       |       700       | 49000     
'''

from datetime import datetime


class Factura:
    # ATRIBUT CONSTANT PENTRU SERIE
    SERIA = 'X'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        # data curenta
        data_azi = datetime.today().strftime('%Y-%m-%d')
        # Calculul totalului
        total = self.cantitate * self.pret_buc

        print(f'Factura seria {self.SERIA} numar {self.numar}')
        print(f'Data: {data_azi}')
        print(f'\nProdus        | Cantitate | Pret bucata | Total')
        print(f'{self.nume_produs.ljust(13)} | {str(self.cantitate).ljust(9)} | {str(self.pret_buc).ljust(12)} | {str(total)}')


factura1 = Factura(numar=1, nume_produs='Telefon', cantitate=7, pret_buc=700)
factura1.genereaza_factura()

# Modificam cateva atribuite
factura1.schimba_cantitatea(10)
factura1.schimba_pretul(750)
factura1.schimba_nume_produs('Laptop')
factura1.genereaza_factura()






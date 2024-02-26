'''
Mașină
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori
disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
descrie() - se vor printa toate atributele, în afară de culori_disponibile
înmatriculare() - va schimba atributul înmatriculată în True
vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile, altfel afișați o eroare
accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
franeaza() - mașina se va opri și va avea viteza 0
'''

class Masina:
    culori_disponibile = {'gri', 'alb', 'negru', 'verde', 'rosu', 'albastu', 'argintiu'}

    def __init__(self, model, viteza_maxima):
        self.marca = 'Alege tu'
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = 'gri'
        self.inmatriculata = False

    def descrie(self):
        print(f'Marca: {self.marca}')
        print(f'Model: {self.model}')
        print(f'Viteza maxima: {self.viteza_maxima}')
        print(f'Viteza actuala: {self.viteza_actuala}')
        print(f'Culoare: {self.culoare}')
        print(f'Inmatriculta: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f'Masina a fost vopsita in culoarea: {culoare}')
        else:
            print(f'Culoarea {culoare} nu este disponibila pentru vopsire')

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Eroare: Viteza nu poate fi negativa')
        elif viteza > self.viteza_maxima:
            print(f'Masina accelereaza pana la viteza maxima {self.viteza_maxima}')
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza
            print(f'Masina a accelerat la viteza {viteza}')

    def franeaza(self):
        self.viteza_actuala = 0
        print('Masina s-a oprit.')


masina1 = Masina(model='Dacia', viteza_maxima=150)
masina1.descrie()

masina1.inmatriculare()
masina1.vopseste('rosu')
masina1.descrie()

masina1.accelereaza(100)
masina1.franeaza()
masina1.accelereaza(-30)
masina1.accelereaza(250)
masina1.descrie()




'''
TodoList
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare. 
Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
Dacă acesta răspunde nu - la revedere
Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
'''
class TodoList:
    def __init__(self):
        self.todo = {}


    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print(f'Task adaugat: {nume}')

    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
            print(f'Task finalizat {nume}')
        else:
            print(f'Task-ul {nume} nu exista in Todo List')

    def afiseaza_todo_list(self):
        print('Todo List: ')
        for nume_task in self.todo.keys():
            print(f'- {nume_task}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            print(f'Detalii pt task-ul {nume_task}: {self.todo[nume_task]}')
        else:
            raspuns = input(f'Task-ul {nume_task} nu exista in Todo List. Doriti sa il adaugati: (da/nu)')
            if raspuns.lower() == 'da':
                descriere_noua = input('Introduceti descrierea pt noul task')
                self.adauga_task(nume_task, descriere_noua)
            else:
                print('La revedere')


todo_list = TodoList()

todo_list.adauga_task('Task1', 'Descriere pentru Task1')
todo_list.adauga_task('Task2', 'Descriere pentru Task2')
todo_list.afiseaza_todo_list()

todo_list.finalizeaza_task('Task1')
todo_list.afiseaza_todo_list()

todo_list.afiseaza_detalii_suplimentare('Task3')
todo_list.afiseaza_detalii_suplimentare('Task2')
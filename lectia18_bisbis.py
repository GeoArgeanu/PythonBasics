import sqlite3

# Conectarea la baza de date
conn = sqlite3.connect('clasa_de_elevi.db')
c = conn.cursor()

# Crearea bazei de date
c.execute('''
    CREATE TABLE elevi11 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nume TEXT NOT NULL,
        note REAL DEFAULT 0,
        absente INTEGER DEFAULT 0
    )
''')

# Adăugarea elevilor
def adauga_elev(nume, note, absente):
    c.execute("INSERT INTO elevi11 (nume, note, absente) VALUES (?, ?, ?)", (nume, note, absente))
    conn.commit()

adauga_elev('Maria Oprisan', 9.5, 3)

# Afișarea listei de elevi
def afiseaza_elevi():
    c.execute("SELECT * FROM elevi10")
    return c.fetchall()

# Actualizarea performanței elevilor
def actualizeaza_elev(id, note, absente):
    c.execute("UPDATE elevi11 SET note = ?, absente = ? WHERE id = ?", [id, note, absente])
    conn.commit()

actualizeaza_elev(1, 10, 6)


# Ștergerea unui elev
def sterge_elev(id):
    c.execute("DELETE FROM elevi11 WHERE id = ?", (id,))
    conn.commit()

sterge_elev(2)

# Raportare performanță clasă
def raportare_performanta():
    c.execute("SELECT AVG(note), AVG(absente) FROM elevi11")
    return c.fetchone()

raportare_performanta()

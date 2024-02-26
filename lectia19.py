'''
Write a SQL statement that groups all countries by continents,
and counts them.
'''

import sqlite3
from acasa_teme import constanta

conn = sqlite3.connect(constanta.DATABASE)
cursor = conn.cursor()
script = '''
CREATE TABLE IF NOT EXIST Continents
'''
'''
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
   3 Schimbări maxime admise:
   Declară o Listă cu 5 jucători
   Schimbari_efectuate = te joci tu cu valori diferite
   Schimbari_max = 3

   Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
   Efectuează schimbarea
   Șterge jucătorul scos din listă
   Adaugă jucătorul intrat
   Afișază a intrat x, a ieșit y, mai ai z schimbări

   Dacă jucătorul nu e în teren:
   Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
   Afișază ‘mai ai z schimbări’

   Testează codul cu diferite valori
'''

jucatori = ['Jucator1', 'Jucator2', 'Jucator3', 'Jucator4', 'Jucator5']
schimbari_efectuate = 0
schimbari_max = 3

print('Echipa de fotbal pt terenul sintetic este:', jucatori)

# SCHIMBAREA 1
if 'Jucator1' in jucatori:
    jucatori.remove('Jucator1')
    jucatori.append('Inloc1')
    schimbari_efectuate += 1
    print(f'A intrat Inloc1 a iesit Jucator1. Mai ai {schimbari_max - schimbari_efectuate}  schimbari')
else:
    print(f'Jucatorul nu e in teren. Mai ai {schimbari_max - schimbari_efectuate} schimbari')


# SCHIMBAREA 2
if 'Jucator2' in jucatori and schimbari_efectuate < schimbari_max:
    jucatori.remove('Jucator2')
    jucatori.append('Inloc2')
    schimbari_efectuate += 1
    print(f'A intrat Inloc2 si a iesit Jucator2. Mai ai {schimbari_max - schimbari_efectuate} schimbari')



# SCHIMBAREA 3
if 'Jucator3' in jucatori and schimbari_efectuate < schimbari_max:
    jucatori.remove('Jucator3')
    jucatori.append('Inloc3')
    schimbari_efectuate += 1
    print(f'A intrat Inloc3 si a iesit Jucator3. Mai ai {schimbari_max - schimbari_efectuate} schimbari')
else:
    print('Nu mai ai schimbari')
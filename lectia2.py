# 2. Verifică și afișează dacă x este număr natural sau nu.

# x = int(input('Introduceti un numar '))
# # verificam daca x e nr nat
# if x >= 0:
#     print(f'{x} este numar natural')
# else:
#     print(f'{x} nu este numar natural')

# x = input('Introduceti un nr: ')
# if x.isdigit():
#     print('Numarul este un nr natural')
# else:
#     print('Numarul nu este un nr natural')




# 3. Verifică și afișează dacă x
# este număr pozitiv, negativ sau neutru.

# x = int(input('Introduceti nr: ')) # int pt nr intregi
#
# if x > 0:
#     print(f'{x} este numar pozitiv')
# elif x == 0:
#     print(f'{x} este numar neutru')
# else:
#     print(f'{x} este numar negativ')




# 4. Verifică și afișează dacă x este între -2 și 13.
# x = int(input('Introdu nr: '))
# if -2 < x < 13:
#     print(f'{x} se afla intre -2 si 13')
# else:
#     print(f'{x} nu se afla in interval')



# 5. Verifică și afișează dacă
# diferența dintre x și y este mai mică de 5.

# x = int(input('Introdu un nr x: '))
# y = int(input('Introdu un nr y: '))
#
# if x - y < 5:
#     print(f'Diferenta dintre {x} si {y} este mai mica de 5')
# else:
#     print(f'Diferenta dintre {x} si {y} nu este mai mica de 5')

# if abs(x - y) < 5:
#     print(f'Diferenta dintre {x} si {y} este mai mica de 5')
# else:
#     print(f'Diferenta dintre {x} si {y} nu este mai mica de 5')



# 6. Verifică dacă x NU este între 5 și 27- a se folosi ‘not’.

# x = int(input('Introdu un nr: '))
# if not (5 < x < 27):
#     print(f'{x} NU este intre 5 si 27')
# else:
#     print(f'{x} se alfa intre 5 si 27')



# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează
# care din ele este mai mare.

x = int(input('Introdu x: '))
y = int(input('Introdu y: '))

if x == y:
    print(f'{x} si {y} sunt egale')
elif x > y:
    print(f'{x} este mai mare decat {y}')
else:
    print(f'{y} este mai mare decat {x}')




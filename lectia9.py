'''
1.Funcție care să calculeze și să returneze suma a două numere
'''


def sum_numbers(a, b):
    rezultat = a + b
    return rezultat


# nr1 = 7
# nr2 = 10
# result_sum = sum_numbers(nr1, nr2)
s = sum_numbers(6, 10)
print(f'Suma nr este {s}')

# print(f'Suma nr {nr1} si {nr2} este {result_sum}')

'''
2. Funcție care să returneze TRUE 
dacă un număr este par, FALSE pentru impar
'''


def even_numbers(number):
    return number % 2 == 0


# VARIANTA SCURTA
nr = even_numbers(13456)
print(nr)

# VARIANTA MAI LUNGA
test_numbers = 7
if even_numbers(test_numbers):
    print(f'{test_numbers} este numar par.')
else:
    print(f'{test_numbers} este numar impar.')

'''
5. Scrieţi o funcţie care returnează prima cifră a unui număr natural. 
De exemplu, dacă parametrul efectiv este 127, funcţia va returna 1.
'''


def first_digit(number):
    while number >= 10:  # nr se imparte repetat la 10 pana cand nr devine mai mic de 10
        number //= 10
    return number


# VARIANTA SCURTA
nr = first_digit(456)
print(f'Prima cifra a nr este {nr}')

# VARIANTA LUNGA
test_nr = 2345
result = first_digit(test_nr)

print(f'Prima cifra a nr {test_nr} este {result}')



'''
6. Să se tipărească toate numerele prime aflate între doi întregi 
citiţi. Programul va folosi o funcţie care testează 
dacă un număr este prim sau nu.
'''

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return  False
#     return  True
#
# def print_primes(start, end):
#     for number in range(start, end + 1):
#         if is_prime(number):
#             print(number)
#
#
# nr = print_primes(1, 100)


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i  == 0:
            return False
    return True

def print_primes(a, b):
    for number in range(a, b + 1):
        if is_prime(number):
            print(number)

limit_inf = -3
limit_sup = 30

print(f'Nr prime intre {limit_inf} si {limit_sup}:')
print_primes(limit_inf, limit_sup)


'''
7. Scrieţi un program care tipăreşte numerele întregi găsite 
între două valori citite, numere care se divid cu suma 
cifrelor lor. Programul va utiliza o funcţie care returnează 
suma cifrelor unui număr întreg primit ca parametru.
'''

def sum_digits(nr):
    sum = 0
    while nr > 0:
        sum += nr % 10
        nr //= 10
    return sum

def print_numbers(start, end):
    for nr in range(start, end + 1):
        if nr % sum_digits(nr) == 0:
            print(nr)


print_numbers(1, 100)


def suma_cifrelor(numar):
    suma = 0
    while numar > 0:
        suma += numar % 10
        numar //= 10
    return suma

def afiseaza_numere_divizibile_cu_suma(limita_inferioara, limita_superioara):
    for numar in range(limita_inferioara, limita_superioara + 1):
        suma = suma_cifrelor(numar)
        if suma != 0 and numar % suma == 0:
            print(numar)

# Exemplu de utilizare:
limita_inferioara = 10
limita_superioara = 100

print(f'Numerele întregi între {limita_inferioara} și {limita_superioara} care se divid cu suma cifrelor lor:')
afiseaza_numere_divizibile_cu_suma(limita_inferioara, limita_superioara)
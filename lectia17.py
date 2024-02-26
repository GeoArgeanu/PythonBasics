'''
1. Sa se genereze primele 100 de numere prime folosind liste, si apoi
folosind generator. Comparati diferenta de timp necesara generarii.
'''

import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Folosind liste
def primes_list(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


# Folosind un generator
def prime_generator(n):
    num = 2
    while n > 0:
        if is_prime(num):
            yield num
            n -= 1
        num += 1


# Masuram timpul pt liste
start_time_list = time.time()
primes = primes_list(100)
end_time_liste = time.time()
print(f'Primele 100 de numere prime folosind liste: {primes}')
print(f'Timpul necesar generarii folosind liste: {end_time_liste - start_time_list} secunde')

# Masuram timpul cu ajutorul unui generator
start_time_generator = time.time()
primes_generator = list(prime_generator(100))
end_time_generator = time.time()
print(f'Primele 100 de numere prime folosind generator: {primes_generator}')
print(f'Timpul necersar generarii folosind generator: {end_time_generator - start_time_generator} secunde')

'''
2. Scrieti un decorator care primeste ca argument numele unui fisier si 
pentru orice functie apelata, el va scrie in acel fisier numele functiei, 
lista de argumente ca si string si rezultatul apelului. Fisierul este de tip csv. 
Functiile decorate pot primi oricate argumente
'''
import csv


def csv_logger(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Apelul functiei
            result = func(*args, **kwargs)

            # Deschidem fisierul CSV in modul de scriere
            with open(file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([func.__name__, str(args), str(kwargs), str(result)])
            return result

        return wrapper

    return decorator


# Exemplu de utilizare a decoratorului
@csv_logger('log.csv')
def add(a, b):
    return a + b


@csv_logger('log.csv')
def add_numbers(x, y):
    return x * y


# Testam functiile decorate
add(2, 3)
add_numbers(4, 5)

'''
3.Sa se creeze un iterator care sa mimice functia enumerate.
ex: 

for index, letter in enumerate('abc'):
    print(f"{index} : {letter}")
'''

class MyEnumerate:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            result = (self.index, self.iterable[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration

# Exemplu de utilizare
for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')

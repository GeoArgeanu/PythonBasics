'''

Creaza o functie Python care inversează și returnează
un număr întreg pozitiv. În cazul unui număr negativ,
afișează o eroare.
Exemple:
reverse(1234567) => 7654321
reverse(10) => 1
reverse(101) => 101
reverse(10000000) => 1
reverse(-65) => eroare

'''

def reverse(n):
    if n < 0:
        return 'Eroare: numarul este negativ'
    else:
        return int(str(n)[::-1])


print(reverse(1234567))
print(reverse(10))
print(reverse(101))
print(reverse(10000000))
print(reverse(-65))
print(reverse(-67789))


'''
Creaza o functie Python care primește o lista și 
un număr întreg pozitiv k, si roteste lista cu k pozitii. 
Exemple:
rotate([1, 2, 3, 4, 5], 2) => [3, 4, 5, 1, 2]
rotate([1, 2, 3, 4, 5], 4) => [5, 1, 2, 3, 4]
rotate([1, 2, 3, 4, 5], 8) => [4, 5, 1, 2, 3]

'''

def rotate(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate([1, 2, 3, 4, 5], 2))
print(rotate([1, 2, 3, 4, 5], 4))
print(rotate([1, 2, 3, 4, 5], 8))
print(rotate([1, 2, 3, 4, 5], 5))


'''
Creaza o functie Python care primește 2 stringuri, 
și verifica dacă acestea sunt anagrame (case-insensitive).
Exemple:
is_anagram(‘Adela’, ‘ealad’) => True
is_anagram(‘ITFactory’, ‘acfiorty’) => True
is_anagram(‘Stringy’, ‘gringsty’) => False
is_anagram(‘ana’, ‘ioana’) => False

'''

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram('Adela', 'ealad'))
print(is_anagram('ITFactory', 'acfiotrty'))
print(is_anagram('Stringy', 'gringsty'))
print(is_anagram('ana', 'ioana'))


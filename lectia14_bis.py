'''
Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
'''

import string
for letter in string.ascii_uppercase:
    filename = letter + '.txt'
    with open(filename, 'w') as file:
        file.write(f' My name is letter {letter}.\n')
        position = string.ascii_uppercase.index(letter) + 1

        if position == 1:
            file.write('I am the 1nd letter of the alphabet.')
        elif position == 2:
            file.write('I am the 2nd letter of the alphabet.')
        elif position == 3:
            file.write('I am the 3nd letter of the alphabet.')
        else:
            file.write(f'I am the {position}nd letter of the alphabet.')








































# import string
# 
# for letter in string.ascii_uppercase:
#     filename = letter + ".txt"
#     with open(filename, "w") as file:
#         file.write(f"My name is letter {letter}.\n")
#         position = string.ascii_uppercase.index(letter) + 1
#         if position == 1:
#             file.write("I am the 1st letter of the alphabet.")
#         elif position == 2:
#             file.write("I am the 2nd letter of the alphabet.")
#         elif position == 3:
#             file.write("I am the 3rd letter of the alphabet.")
#         else:
#             file.write(f"I am the {position}th letter of the alphabet.")

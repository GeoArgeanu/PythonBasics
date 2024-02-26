'''
Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file
'''
def write(filename):
    with open('hello.text', 'w') as file:
        # \n de a le trece una sub alta
        file.write('Python\nJava\nJavascript\nC/C++/C#\nPHP\nNode.js')



with open('hello.text', 'r') as file:
    file_contents = file.read()
    print(file_contents)
    print('-'* 20)


# Read and display the contents of the hello.txt file

# with open('hello.text', 'r') as file:
#     file_contents = file.read()
#     print(file_contents)


'''
Write a short program to append the following lines to “hello.txt” 
(you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
Display the new contents of the file.
'''
# List of string to append
new_lines = ['Go', 'Kotlin', 'Swift']

# Append the new lines to hello.txt
# with open('hello.text', 'a') as file:
#     for line in new_lines:
#         file.write(line + '\n')

# Read and display the updated contents of hello.txt
# with open('hello.text', 'r') as file:
#     updated_contents = file.read()
# print(updated_contents)



'''
Write a short program that reads the “hello.txt” file and 
displays every other line (only odd lines).
'''
# Varianta 1
with open('hello.text', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        print(lines[i])

# Varianta 2
file_path = 'hello.text'
try:
    with open('file_path', 'r') as file:
        lines = file.readlines()
        odd_lines = lines[::2]  # Get every other line (odd lines)

        for line in odd_lines:
            print(line.strip())  # strip any leading or trailing witespace


except FileNotFoundError:
    print(f'File {file_path} not found.')
except Exception as e:
    print(f'An error occurred: {e}')


'''
Write a program that generates 26 text files, called 
`A.txt`, `B.txt`, … `Z.txt`. Each file will contain 
the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s 
number (e.g. 1st, 2nd, 3rd, etc.)
'''

import os

def ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return str(number) + suffix

# Create a directory to store the files
directory = "alphabet_files"
os.makedirs(directory, exist_ok=True)

# Generate files from A.txt to Z.txt
for i in range(1, 27):
    letter = chr(ord('A') + i - 1)
    filename = os.path.join(directory, f"{letter}.txt")

    with open(filename, "w") as file:
        file.write(f"My name is letter {letter}.\n")
        file.write(f"I am the {ordinal(i)} letter of the alphabet.\n")

print("Files created successfully in the 'alphabet_files' directory.")


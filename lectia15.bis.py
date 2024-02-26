'''
Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
Read the file using Python’s `csv` standard library,
and display it in the terminal as a table, using the
options for string formatting from Python:

id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu		21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa			29	9.0

'''

import csv

# Create the students.csv file
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'fname', 'lname', 'age', 'grade'])
    data = [
        [1, 'Maria', 'Popescu', 31, 7.5],
        [2, 'Andrei', 'Ionescu', 26, 8.0],
        [3, 'Adriana', 'Marinescu', 21, 7.5],
        [4, 'Matei', 'Gheorghescu', 42, 8.5],
        [5, 'Eusebiu', 'Pop', 33, 9.5],
        [6, 'Ioana', 'Popa', 29, 9.0],
    ]
    writer.writerows(data)

# Read and display the content as a table
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    # Calculate column widths for formatting
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(header, *zip(*reader))]

    # Print header
    print("  ".join(f"{col:{width}}" for col, width in zip(header, col_widths)))
    print("-" * (sum(col_widths) + len(header) * 2))

    # Print rows
    file.seek(0)
    next(reader)  # Skip header for data rows
    for row in reader:
        print("  ".join(f"{cell:{width}}" for cell, width in zip(row, col_widths)))
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
import json

# Define the data to be written
data = [
    ["id", "fname", "lname", "age", "grade"],
    [1, "Maria", "Popescu", 31, 7.5],
    [2, "Andrei", "Ionescu", 26, 8.0],
    [3, "Adriana", "Marinescu", 21, 7.5],
    [4, "Matei", "Gheorghescu", 42, 8.5],
    [5, "Eusebiu", "Pop", 33, 9.5],
    [6, "Ioana", "Popa", 29, 9.0]
]

# Write the data to a CSV file
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read the CSV file and display it as a table
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('{:<5} {:<10} {:<10} {:<5} {}'.format(*header))
    print('-' * 50)
    for row in reader:
        print('{:<5} {:<10} {:<10} {:<5} {}'.format(*row))

'''
Read again the information from the csv file above, store it all in a list of data, 
and then write a new file, called “students.json”, which will contain a valid JSON object. 
Use the following format for each student (and use Python’s standard JSON module):
[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5	
	},
	...
]

'''
# Read the data from the CSV file and store it in a list

data = []
with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# Write the data to a JSON file
with open('students.csv', 'w') as f:
    json.dump(data, f, indent=4)

print("Data has been successfully written to students.json.")


'''
Create a class called Student, based on the data above. Read the JSON file 
you created, and load all the data into a list of Student objects. 
Add a few more Student objects to the list, and then write the new list in a new JSON file.
'''

class Student:
    def __init__(self, id, fname, lname, age, grade):
        self.id = int(id)
        self.fname = fname
        self.lname = lname
        self.age = int(age)
        self.grade = float(grade)

    def to_dict(self):
        return {
            'id':self.id,
            'fname':self.fname,
            'lname':self.lname,
            'age':self.age,
            'grade':self.grade
        }

with open('students.csv', 'r') as f:
    data = json.load(f)

students_list = [Student(**student) for student in data]

students_list.extend([
    Student(7, 'Alex', 'Popescu', 25, 8.3),
    Student(8, 'Victor', 'Ionescu', 28, 9.5),
    Student(9, 'Razvan', 'Argeanu', 22, 7.8)
])

updated_students_data = [student.to_dict() for student in students_list]

with open('updated_students.json', 'w') as updated_json_file:
    json.dump(updated_students_data, updated_json_file, indent=4)


print("Data has been successfully written to updated_students.json.")




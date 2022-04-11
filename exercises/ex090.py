# EX 090: Write a program that will store, in a dictionary, the name, grades, and status of a student,
# where the approval grade is 7.
D = {'name': str(input('What is the student name?')),
     'grade': int(input('What is the students grade?')),
     'status': 'Not Approved'}
if D['grade'] >= 7:
    D['status'] = 'Approved'

for a, b in D.items():
    print(f'The {a} is {b}')


# EX 069: Create a program that will read the gender and the age of several people. Then show:
# A) How many people are over 18 years old;
# B) How many men are there;
# C) How many women are under 20 years old
countA = countB = countC = 0
while True:
    name = str(input('Name?'))
    age = int(input('Age?'))
    gender = str(input('Gender? [Male//Female]')).strip().upper()[0]
    while gender not in 'MF':
        print('INVALID RESPONSE MY DUDE')
        gender = str(input('Gender? [Male//Female]')).strip().upper()[0]
    if gender == 'F' and age < 20:
        countC += 1
    if gender == 'M':
        countB += 1
    if age > 18:
        countA += 1
    ask = str(input('Do you wish to add another person to this list? [Y // N]')).strip().upper()[0]
    if ask in 'N':
        break
print(f'There are {countA} people over 18 y/o, {countB} men, and {countC} women under 20 y/o.')


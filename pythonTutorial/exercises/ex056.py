"""ex 056: write a script that will read the names, ages and genders of 4 people"""
age = [0, 0, 0, 0]
gend = ['', '', '', '']
name = ['', '', '', '']
eldest = ''
women = 0
for c in range(0, 4):
    name[c] = str(input('Whats your name?')).strip()
    age[c] = int(input('How old are you?'))
    if age[c] > age[c-1]:
        eldest = c
    gend[c] = str(input('Whats your gender? M or F')).strip()
    if gend[c] in 'Ff':
        if age[c] <= 20:
            women += 1
aa = (age[0] + age[1] + age[2] + age[3]) / 4
print('The average age of these people is {} years old.'.format(aa))
print('The oldest person is {}'.format(name[eldest]))
print('{} women are younger than 20 y/o.'.format(women))

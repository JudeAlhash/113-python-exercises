# EX 094 : Make a script that will store each person's infos on a dictionary, and store each dictionary on a list.
# Ask for: Name, sex and age. Then, provide the following: Total people registered, the average age, a list with
# all the women, and lastly, a list with all the ages above the average age.

database = []
womenList = []
count = totalAge = 0
while True:     # I have created the dict() directly inside the list, it would be clearer to make the dictionary first,
    count += 1  # and then, add them to the list..
    database.append({                                                            # Receiving Age and Name inputs
        f'name': str(input('What is your name?')).strip(),
        f'age': int(input('What is your age?')),
    })
    gender = str(input('What is your gender?(M or F)')).lower().strip()[0]       # Receiving and validating Gender input
    while gender not in 'mf':
        gender = str(input('What is your gender?(M or F)')).lower().strip()[0]
    database[count-1][f'gender'] = gender
    check = str(input('Would you like to keep going? (Yes or No)')).lower().strip()[0]
    while check not in 'yn':
        check = str(input('Would you like to keep going? (Yes or No)')).lower().strip()[0]
    if check == 'n':
        break

for c in range(0, len(database)):
    for k, v in database[c].items():
        if 'age' in k:
            totalAge += v
        if 'gender' in k:
            if 'f' in v:
                womenList.append(database[c]['name'])


print(f'All women in the list:{womenList}')
print(f'Total number of people registered: {len(database)}\n'
      f'Average Age: {totalAge/len(database):.2f}')
print('People aged above average:')
for g in range(0, len(database)):
    if database[g]['age'] > (totalAge/len(database)):
        print(database[g]['name'], end=';')
        print(f' Age : {database[g]["age"]}', end=';')
        print(f' Gender:{database[g]["gender"].upper()}')
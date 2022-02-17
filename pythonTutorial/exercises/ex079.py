# EX 079 : Create a program where the user types in numbers, and they get added into a list,
# UNLESS the number has already been added. This goes until the user desires.
L = []
while True:
    n = int(input('Choose a number to be added to the list.'))
    if n not in L:
        L.append(n)
        print('Value added successfully')
    else:
        print('Duplicate Value, cannot be added...')
    check = str(input('Would you like to go on? [Yes or No]')).strip().lower()[0]
    if check == 'n':
        break

print(sorted(L))  # TEST: sorted() does not modify the list, while .sort() does.
print(L)
L.sort()
print(L)

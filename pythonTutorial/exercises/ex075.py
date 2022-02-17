# EX 075 : DATA ANALYSIS WITH TUPLES. Receive 4 values from the user, and store them into a tuple. Then, show me:
# How many times 9 showed up; What position is the 3 in; All the even numbers we have.

#LISTS RESOLUTION
print('Provide me with four values:')
v = [0, 0, 0, 0]
for c in range(0, 4):
    v[c] = input(f'Value number {c+1}: ')
    while v[c] == '':
        v[c] = input(f'Please, give me a value.')
    v[c] = int(v[c])
print(v)
print(f'The number 9 shows up {v.count(9)} times.')
if v[0] == 3 or v[1] == 3 or v[2] == 3 or v[3] == 3:
    print(f'The number 3 shows up in position {v.index(3)}.')
else:
    print('We don`t have a number three.')
print(f'We have the following even numbers:')
for g in v:
    if g % 2 == 0:
        print(g)

#TUPLE RESOLUTION
v1 = int(input('Give me value 1:'))
v2 = int(input('Give me value 2:'))
v3 = int(input('Give me value 3:'))
v4 = int(input('Give me value 4:'))
tup = (v1, v2, v3, v4)
print(f'The number 9 shows up {tup.count(9)} times.')
if tup[0] == 3 or tup[1] == 3 or tup[2] == 3 or tup[3] == 3:
    print(f'The number 3 shows up in position {tup.index(3)}.')
else:
    print('We don`t have a number three.')
print(f'We have the following even numbers:')
for n in tup:
    if n % 2 == 0:
        print(n, end='')
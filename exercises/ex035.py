'''Have the user input 3 lengths, and discover if those lines could form a triangle.'''

l1 = float(input('Give me the length of three lines.\n1:'))
l2 = float(input('2:'))
l3 = float(input('3:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('You got a triangle!')
else:
    print('We don`t got no triangle, no sir')
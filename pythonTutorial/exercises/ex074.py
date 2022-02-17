# EX 074 : Write a script that will produce 5 random numbers inside a tuple, then show me the list, the biggest one,
# and the smallest one.
from random import randint
r = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), )
print(r)
print(f'The smallest item of the list is {sorted(r)[0]}')
print(f'The biggest item of the list is {sorted(r)[4]}')

# You could have also used max() and min()
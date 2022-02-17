# EX 076 : Make a program with a single tuple that stores several item names, and also their respective prices.
# Then, make a table for them.
# Remake this one eventually? Table making-a$s exercise dude

tup = ('Pencil', 3.99,
       'Pen', 1.99,
       'Book', 10.99,
       'Car', 4000,
       'Sandwich', 2.99)
print('-'*40)
print('Table of Prices')
print('-'*40)
for c in range(0, len(tup)):
    if c % 2 == 0:
        print(f'{tup[c]:.<30}', end='')
    else:
        print(f'${tup[c]:>8.2f}')
print('-'*40)
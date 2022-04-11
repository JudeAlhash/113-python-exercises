# EX 080 : Write a program where the user adds 5 values to a list, already in the correct order (Without sort()).
# Then show the list.

# SECOND TRY

L = []
for c in range(0, 5):
    n = int(input(f'Give me value n {c+1}: '))
    if c == 0 or n >= L[-1]:
        L.append(n)
        print(f'The number was added to the end of the list.')
    else:
        pos = 0
        while pos < len(L):
            if n <= L[pos]:
                L.insert(pos, n)
                print(f'The number {n} was added to position {pos} of the list.')
                break
            pos += 1
print(L)


"""
CORRECT RESULTS, INEFFICIENT METHOD. TRY AGAIN
L = []
for c in range(0, 4):
    n = int(input(f'Give me value n{c+1}'))
    if c == 0:
        L.append(n)
        print(f'Number {n} was added successfully.')
    if c == 1:
        if n >= L[0]:
            L.append(n)
            print(f'The number {n} was added to the end of the list.')
        elif n < L[0]:
            L.insert(0, n)
            print(f'The number was added to the {0} position of the list.')
    if c == 2:
        if n >= L[1]:
            L.append(n)
            print(f'The number {n} was added to the end of the list.')
        elif n < L[0]:
            L.insert(0, n)
            print(f'The number was added to the {0} position of the list.')
        elif L[1] > n > L[0]:
            L.insert(1, n)
            print(f'The number was added to the second position of the list.')
    if c == 3:
        if n >= L[2]:
            L.append(n)
            print(f'The number {n} was added to the end of the list.')
        elif n < L[0]:
            L.insert(0, n)
            print(f'The number was added to the first position of the list.')
        elif L[1] > n >= L[0]:
            L.insert(1, n)
            print(f'The number was added to the second position of the list.')
        elif L[2] > n >= L[1]:
            L.insert(2, n)
            print('fThe number was added to the third position of the list.')
print(L)
"""


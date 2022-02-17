# EX 086 : Create a 3 x 3 MATRIX where the user chooses all the data for it.

matrix = [[], [], []]
for b in range(0, 3):
    for c in range(0, 3):
        matrix[b].append(int(input(f'Pick a value for the position {b,c}: ')))
print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}')

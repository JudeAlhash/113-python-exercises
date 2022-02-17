# EX 087 : MORE MATRIX! Remake the 3 x 3 matrix, and then show me: The sum of all the even values,
# the sum of the third row, and the largest value of the second row.
matrix = [[], [], []]
s = g = a = 0
for b in range(0, 3):
    for c in range(0, 3):
        matrix[b].append(int(input(f'Input a value for {b,c}')))
        if matrix[b][c] % 2 == 0:
            a += matrix[b][c]
        if b == 2:
            s += matrix[2][c]
        if b == 1:
            if g < matrix[1][c]:
                g = matrix[1][c]
print(f'The sum of all the elements in the third row is {s}')
print(f'The greatest element in the second row is {g}')
print(f'The sum of all even elements in the matrix is {a}')



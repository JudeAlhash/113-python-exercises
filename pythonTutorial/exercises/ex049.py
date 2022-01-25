# Make a program that will receive a number, and then show us its multiplications from 0 to 10.

m = int(input('Give me a number.'))
for c in range(0, 11):
    print("{} X {} = {}".format(c, m, c*m))

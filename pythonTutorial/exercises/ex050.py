"""EX 050: Develop a program that will receive six integer values from the user,
and show the sum only of the EVEN numbers."""

s = 0
count = 0
for c in range(0, 6):
    n = int(input('Type in a number.'))
    if n % 2 == 0:
        s += n
        count += 1
print('The sum between the {} EVEN given values is {}'.format(count, s))

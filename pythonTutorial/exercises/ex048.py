""" EX 048: Write a script that will calculate the sum between all the UNEVEN numbers that are multiples of 3,
and are in between 1 and 500."""

s = 0
count = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        s += c
        count += 1
print('The sum between all the multiples of 3 from 0 to 500 is {}, and the total number of numbers is {}'.format(s, count))
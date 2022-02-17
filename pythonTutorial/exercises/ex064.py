# EX 064: Write a program that will receive several integer inputs. When the user types 999, the program ends and sums
# the other values.
a = c = count = 0
while c != 999:
    c = int(input('Which number would you like to add?'))
    if c != 999:
        count += 1
        a += c
print('The sum of all the {} numbers is equal to {}.'.format(count, a))

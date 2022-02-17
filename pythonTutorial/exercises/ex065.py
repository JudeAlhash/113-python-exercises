# EX 065: Create a script that reads multiple integer values from user, and asks if he wants to keep going.
# Then, show the average between all the values, and also which were the biggest and smallest value amongst them.
a = int(input('What number do you choose?'))
small = large = a
total = count = 0
can = ''
while can != 'N':
    if a > large:
        large = a
    elif a < small:
        small = a
    total += a
    count += 1
    can = str(input('Would you like to keep going?[y // n]')).strip().upper()[0]
    if can != 'N':
        a = int(input('What number do you choose?'))
ave = total / count
print('The biggest number is {}, the smallest, {}, and the average is {}'.format(large, small, ave))

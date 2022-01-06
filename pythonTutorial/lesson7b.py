n1 = int(input('Type in any number.'))
n2 = int(input('Now, another one.'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print('The sum between the two numbers is {}, and the multiplication is {}. \n'.format(s, m), end='')

print('The division between the two numbers is {:.3f}, and the integer division is {}. The first number elevated to the second number`s power would be {}.'.format(d, di, p)) 


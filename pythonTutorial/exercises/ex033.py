"""Write a script that will receive 3 values, and determine which is the largest, and which is the smallest."""

'''MY SOLUTION;
L = 0
a = int(input('Give me three values, and I will determine the largest and the smallest from among them. \nFirst value:'))
if a > L:
    L = a
S = a
a = int(input('Second value:'))
if a > L:
    L = a
if a < S:
    S = a
a = int(input('Third value:'))
if a > L:
    L = a
if a < S:
    S = a
print('The largest number is {}, and the smallest {}.'.format(L, S))
'''
#Prof Solution:
a = int(input('Give me a value.'))
b = int(input('Another one.'))
c = int(input('Third value, please.'))

L = a
if b > a and b > c:
    L = b
if c > a and c > b:
    L = c

S = a
if b < a and b < c:
    S = b
if c < a and c < b:
    S = c

print('The biggest number is {} and the smallest number is {}.'.format(L, S))

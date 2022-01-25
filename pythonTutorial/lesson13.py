# LOOPS: LESSON 13
"""
for c in range(6, 0, -1):
    print(c)
print('END')

s = int(input('Start at:'))
e = int(input('End at:'))
i = int(input('Iteration:'))
for c in range(s, e + 1, i):
    print(c)
print('FIM')
"""

s = 0
for c in range(0,4):
    n = int(input('Type in a number:'))
    s += n
print('The sum of all these numbers is {}'.format(s))
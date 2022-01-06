# 019. Help the teacher pick out one of his 4 students at random to clean the white board.
import random

n2 = str(input('First Student: '))
n3 = str(input('Second Student: '))
n4 = str(input('Third Student: '))
n5 = str(input('Fourth Student: '))
L = [n2, n3, n4, n5]

chosen = random.choice(L)
print('The chosen student is {}.'.format(chosen))
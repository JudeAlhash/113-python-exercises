# 016. Read a real number, and show its integer portion.
# f = float(input('Give me a real number.'))
# i = int(f)
# print('The typed number is {}, and its integer portion is {}.'.float(f, i))
import math
f = float(input('Give me a real number.'))
print('The typed number is {}. The integer portion of it would be {}.'.format(f, math.trunc(f)))
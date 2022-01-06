import math
# 017. Receive inputs to determine the length of the minor and major catheti of a triangle. Use the information to
# calculate the length of the hypotenuse.
mj = float(input('What is the length of the major cathetus of the triangle?'))
mn = float(input('What about the minor cathetus?'))
# h = math.sqrt(mj**2 + mn**2)
h = math.hypot(mj, mn)
print('The hypotenuse length is {:.3f}.'.format(h))
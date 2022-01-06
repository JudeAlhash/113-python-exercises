import math

# 018. Receive an angle value, and determine the value of the sine, cossene and tangent.
a = int(input('Give me an angle, and I will convert it to show the sine, cossene and tangent values correspondent to '
              'it.'))
print('sin = {:.4f}, cos = {:.4f}, tan = {:.4f}'.format(math.sin(math.radians(a)), math.cos(math.radians(a)),
                                                        math.tan(math.radians(a))))

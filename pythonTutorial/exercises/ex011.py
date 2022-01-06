# 011: Write a script that reads the height and width of a wall, calculates its area,
# and tells me how much paint I will need if each liter covers 2 square meters.
h = float(input('How tall is this wall, new guy?'))
w = float(input('And how wide is it?'))
a = h * w
l = a / 2
print('Go get us about {} liters of paint for this wall, then. Chop chop.'.format(l))
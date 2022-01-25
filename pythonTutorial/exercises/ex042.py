#Determins if three lines can make a triangle, and , if yes, determine which type of triangle it is.
print('How long are the lines of your proposed triangle?')
a = float(input('Line A:'))
b = float(input('Line B:'))
c = float(input('Line C:'))
if a < b + c and b < c + a and c < a + b:
    if a == b == c:
        print('This triangle is equilateral, because all the sides are the same length.')
    elif a == b or a == c or c == b:
        print('This triangle is an isosceles triangle, because 2 of its sides are of the same length.')
    elif a != b != c:
        print('This triangle is Scalene, because the sides are all different lengths.')
else:
    print('These lines cannot form a triangle.')
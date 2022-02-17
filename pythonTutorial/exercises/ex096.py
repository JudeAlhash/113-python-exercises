# EX 096 : Make a function that calculates the area of a rectangle.
def area(a, b):
    c = a * b
    print(f'The area for this rectangle is {c}m^2.')


area(int(input('What is the length of this rectangle in meters?')), int(input('And what is the width?')))

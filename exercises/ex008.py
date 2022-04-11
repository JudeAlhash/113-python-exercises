# 008: Write a script that reads a value in meters, and the show the converted value in centimeters and milimeters.
a = int(input('Give me a meter measurement.'))
ac = a * 100
am = a * 1000
print('Converted to centimeters and meters, the values would be {}cm and {}mm.'.format(ac, am))
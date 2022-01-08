"""Write a script that will receive a year from the user, and tell him if it is a leap year or not."""
y = int(input('Type in any year.'))
leap = y % 4
if leap == 0 and y % 100 != 0 or y % 400 == 0:
    print('This is a leap year.')
else:
    print('This is not a leap year.')


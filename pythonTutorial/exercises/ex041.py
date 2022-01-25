"""The Swimmer's association needs a program to determine in which category their athletes fall into.
Up to 9 years old: Kid
Up to 14 years old: Teen
Up to 19 years old: Young Adult
Up to 25 years old: Senior
More than 25: Master"""

age = int(input('What is your age?'))

if age < 9:
    print('Classification: Kid')
elif 9 <= age < 14:
    print('Classification: Teen')
elif 14 <= age < 19:
    print('Classification: Young Adult')
elif 19 <= age < 25:
    print('Classification: Senior')
elif age >= 25:
    print('Classification: Master')
#Write a script that will read 2 integers and compare them, and shows which one is bigger, or if they're equivalent.

one = int(input('Give me a number.'))
two = int(input('Give me another number.'))

if one == two:
    print('The two numbers are equivalent.')
elif one > two:
    print('{} is the biggest between the two.'.format(one))
else:
    print('{} is the biggest between the two.'.format(two))
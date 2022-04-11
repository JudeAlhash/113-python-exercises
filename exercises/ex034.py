""" Write a script that will calculate the raise of someone's salary. If the person earns more than $1250, the raise is
of 10%. If the person's salary is smaller than $1250, the raise if of 15%."""
s = int(input('What is your monthly salary?'))
if s > 1250:
    print('Your new salary is {}, you got a 10% raise.'.format(s*1.10))
else:
    print('Your new salary is {}, you got a 15% raise.'.format(s*1.15))

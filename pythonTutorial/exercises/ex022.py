# Write a script that will read a person's full name, then repeat it back all in caps, then all in lower case,
# shows how many letters there are in total, and then in the first name.

name = str(input('What is your full name?')).strip()
print('Your name in caps is {}'.format(name.upper()))
print('Your name in lower case is {}'.format(name.lower()))
print('Your name has {} letters.'.format(len(name) - name.count(' ')))
print('Your first name has {} letters.'.format(name.find(' ')))




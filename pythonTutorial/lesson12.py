#Lesson 12; nested conditions

name = str(input('What`s your name?')).strip()
if name == 'Paulo':
    print('What a beautiful name!')
elif name == 'Pedro' or name == 'Maria':
    print('Your name is very popular in Brazil.')
else:
    print('Very basic name.')
print('Have a good day.')

# EX 057: INPUT VALIDATION - QUESTION ABOUT GENDER ONLY ACCEPTS M OR F
gender = str(input('What is your gender? [M or F]')).strip().upper()[0]
while gender not in 'MF':
    gender = str(input('INVALID INPUT. What is your gender?')).strip().upper()[0]
print('Your gender is {}'.format(gender))
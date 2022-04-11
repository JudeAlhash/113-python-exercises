#Ask for the user's weight and height to calculate the user's BMI and tell them what health classification they're in.
"""
Classifications:
Under 18.5 - Below Ideal Weight
Between 18.5 and 25 - Ideal Weight
Between 25 and 30 - Above Ideal Weight
Between 30 and 40 - Obesity
Above 40 - Morbid Obesity
"""
w = float(input('How much do you weigh?'))
h = float(input('How tall are you (in meters)?'))

BMI = w / (h ** 2)

if BMI < 18.5:
    print('Below Ideal Weight')
elif 18.5 <= BMI < 25:
    print('Ideal Weight')
elif 25 <= BMI < 30:
    print('Above Ideal Weight')
elif 30 <= BMI < 40:
    print('Obesity')
else:
    print('Morbid Obesity')
print('Your BMI is {:.2f}.'.format(BMI))
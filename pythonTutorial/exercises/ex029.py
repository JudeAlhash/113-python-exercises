# Write a script that will receive a speed reading in mph. Then, analyze wether it is going at an acceptable speed, or
#going too fast.
speed = int(input('How fast were you going, sir?'))
if speed > 60:
    print('Fined! You were going over the limit. Cough me up ${}, will ya.'.format((speed - 60) * 7))
print('Have a good day sir, stay safe.')

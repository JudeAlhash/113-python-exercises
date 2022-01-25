# Write a script that will ask for the age of 7 different people. Then, tell me how many of these people are underage.
from datetime import date
y = 0
o = 0
for c in range(0, 7):
    answer = int(input('What year were you born?'))
    age = date.today().year - answer
    if age >= 18:
        o += 1
    else:
        y += 1
print('{} people are underage, and {} people are 18 or older.'.format(y, o))
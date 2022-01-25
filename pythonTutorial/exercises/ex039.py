"""Write a script that will ask for a person's age, and then analyze how much time he has left before he needs to enlist
 in the army, how long ago he should have enlisted, or if he needs to do it this year."""
from datetime import date
present = date.today().year
year = int(input('What year were you born?'))
age = present - year
if age == 18:
    print('The time to enlist is Right Now!')
elif age < 18:
    print('You still have {} years before you have to enlist.'.format(18-age))
else:
    print('You should have enlisted {} years ago! Move it, get it done ASAP.'.format(age-18))
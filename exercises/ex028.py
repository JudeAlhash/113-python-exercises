# Write a script that will make the computer think of a number from 0 to 5, and then asks for you to guess which one
# it was, as a game.

import random
x = random.randint(0, 5)
y = int(input('Type a number from 0 to 5, try to guess which one I picked.'))
print('Processing . . . . . . .')
sleep(3)
if (x == y) :
    print('Congratulations, you win the game.')
else:
    print('Ah ha! I win, once again. I thought of {}, and you guessed {}. computers > humans'.format(x, y))
# CODE A ROCK PAPER SCISSOR GAME
from random import randint
from time import sleep

items = ('Rock', 'Paper', 'Scissor')

j = int(input('''
[0] to play ROCK
[1] to play PAPER
[2] to play SCISSOR
'''))
k = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('Player threw {}, PC threw {}'.format(items[j], items[k]))
if j == k:
    print('Draw!')
else:
    if j == 0 and k == 2:
        print('Player WINS!')
    elif j == 0 and k == 1:
        print('PC wins!')
    elif j == 1 and k == 0:
        print('Player WINS!')
    elif j == 1 and k == 2:
        print('PC wins!')
    elif j == 2 and k == 0:
        print('PC wins!')
    elif j == 2 and k == 1:
        print('Player WINS!')

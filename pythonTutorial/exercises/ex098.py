# EX 098 : Create a function that will: a. count from one to ten; b. count from 10 to 0, pace 2; c. count starting
# from the number the user requested, to the number a user requested, in their desired pace.
from time import sleep


def count(a, b, c):
    if c == 0:
        c = 1
    if b < a and c >= 0:
        c = -c
    if a < b and c < 0:
        c = -c
    print('=-' * 12)
    for c in range(a, b, c):
        print(c, end=' ')
        sleep(.3)
    print()


count(1, 10, 1)
count(10, 0, -2)
count(int(input('What number should we start counting from?')), int(input('Should we count up to what number?')),
      int(input('In what pace should we count?')))

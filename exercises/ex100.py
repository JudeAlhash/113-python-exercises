# EX 100 : Write a script that has a list, and two functions that interact with the list. The first function will
# randomize 5 numbers and put them into the list, and the second function will sum all the even numbers in the list.
from random import randint


def evenSum(list):
    even = 0
    for b in list:
        if b % 2 == 0:
            even += b
    print(f'Sum of the even numbers of the list: {even}')


def randomize(l):
    randList.clear()
    for c in range(0, l):
        randList.append(randint(0, 10))
    print(randList)


randList = list()
while True:
    randomize(int(input('How many items do you want in the randomized list?')))
    evenSum(randList)
    check = str(input('Again? [y//n]')).strip().lower()
    if check == 'n':
        break
# EX 088 : Make a script that will generate several lists with different numbers (lottery style). It should generate
# however many lottery tickets the user requests, with 6 separate values in between 0 and 60, without repeating
# themselves, and also storing all of them into a list.
from random import randint
from time import sleep
ticketGroup = []
ticketSingle = []
randcheck = 0
gamesquant = int(input('How many games would you like to play?'))
for t in range(0, gamesquant):
    for c in range(0, 6):
        randcheck = randint(1, 6)
        print(randcheck)
        while randcheck in ticketSingle:
            randcheck = randint(1, 6)
        ticketSingle.append(randcheck)
    ticketGroup.append(ticketSingle[:])
    print(ticketSingle)
    #print(ticketSingle)
    sleep(0.5)
    ticketSingle.clear()
#print(f'You purchased {len(ticketGroup)} tickets. Here they are:\n{ticketGroup}')
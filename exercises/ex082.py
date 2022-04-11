# EX 082 : Create a script that will receive values from the user, and create 3 lists: on with all the values, another
# with the even numbers between the values, and the last one with the uneven numbers. Stops when user decides to.
L = []
evL = []
unL = []
while True:
    n = int(input('Type in any number.'))
    L.append(n)
    if n % 2 == 0:
        evL.append(n)
    else:
        unL.append(n)
    check = str(input('If you would like to stop now, input [N]. Otherwise, input any value.')).strip().lower()[0]
    if check == 'n':
        break
print(f'Complete List: {L}')
print(f'Even List: {evL}')
print(f'Uneven list: {unL}')

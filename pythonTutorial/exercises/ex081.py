# EX 081 : Make a script that will receive inputs from the user until they decide to stop, and put them into a list.
# Then, show how many numbers were added to the list, show the list in reverse order, and show if 5 is present.
L = []
while True:
    L.append(int(input('What value would you like to add?')))
    check = str(input('Would you like to keep going? [Yes or No]')).strip().lower()[0]
    if check == 'n':
        break
print(f'There are {len(L)} values inside this list.')
L.sort(reverse=True)
print(L)
if 5 in L:
    print('Yes, there is on or more instances of the number 5 in this list.')
else:
    print('Number 5 is not on this list.')
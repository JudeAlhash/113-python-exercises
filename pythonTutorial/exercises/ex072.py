# EX 072 : Create a tuple that contains every number, written out as a string. Then make a program that will ask the
# user which number he wants to see written.

n = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
     'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    c = (int(input('Which number, from 0 to 20, would you like to see written out?')))
    while not 0 <= c <= 20:
        c = (int(input('Which number, FROM ZERO TO TWENTY, would you like to see written out?')))
    print(f'You chose the number {n[c]}')
    k = str(input('Would you like to keep going? [Yes or No]')).strip().lower()[0]
    if k == 'n':
        break

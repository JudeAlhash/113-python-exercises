"""Write a script that will read 2 values from the user, and show a menu of options of what to do with the numbers.
1 - SUM
2 - MULTIPLY
3 - BIGGEST
4 - NEW VALUES
5 - EXIT PROGRAM
"""
v1 = int(input('Pick a value, any value!'))
v2 = int(input('Another one.'))
pare = False
while not pare:
    choice = int(input("""What do you want to do with the numbers?
    [1] ADD
    [2] MULTIPLY
    [3] BIGGEST
    [4] NEW NUMBERS
    [5] EXIT THE PROGRAM"""))
    while not 1 <= choice <= 5:
        choice = int(input('Invalid entry! Choose one of the menu options.'))
    if choice == 1:
        print(v1 + v2)
    elif choice == 2:
        print(v1 * v2)
    elif choice == 3:
        if v1 > v2:
            print('{} is the biggest number.'.format(v1))
        elif v1 < v2:
            print('{} is the biggest number.'.format(v2))
        else:
            print('The numbers are equal.')
    elif choice == 4:
        v1 = int(input('What is the first value?'))
        v2 = int(input('What about the second one?'))
    elif choice == 5:
        print('turning off...')
        pare = True
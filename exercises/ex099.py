# EX 099 : CREATE A SCRIPT THAT WILL RECEIVE AN INDEFINITE AMOUNT OF PARAMETERS/ARGUMENTS, THEN SHOW THE LARGEST VALUE.

def bigger(*num):
    print('-' * 30)
    big = 0
    if len(num) == 1 and num[0] == 0 or len(num) == 0:
        print('No valid values entered.')
    else:
        for c in range(0, len(num)):
            print(num[c], end=', ')
            if num[c] > big:
                big = num[c]
        print(f'total numbers entered: {len(num)}\nBiggest number entered: {big}')
    #print(max(num))


bigger(1, 2, 3, 4)
bigger(10, 4, 2, 1)
bigger(0)
bigger()
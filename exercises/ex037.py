"""Make a conversion system for numeric bases. I need you to be able to transform any given number into its Octal,
Binary or Hexadecimal Base Equivalent in the following manner:
Press [1] for Binary
Press [2] for Octal
Press [3] for Hexadecimal"""

n = int(input('Give me any number.'))
i = str(input('Press [1] for the binary equivalent of {}; \nPress [2] for the octal equivalent of {}\nPress [3] for '
              'the hexadecimal equivalent of {}\n'.format(n,n,n))).strip()

if i == '1':
    print('{} in binary would be {}.'.format(n, bin(n)[2:]))
elif i == '2':
    print('{} in octal base would be {}.'.format(n, oct(n)[2:]))
elif i == '3':
    print('{} in hexadecimal base would be {}.'.format(n, hex(n)[2:]))
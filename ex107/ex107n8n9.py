# EX 107 : Make your own module package, with the following functions: calculate half of the given value; double of
# given value; increase value by X%; decrease value by X%.
# EX 108 : Adapt the module's code to include money(), a function to format the way the values are being displayed.
# EX 109 : Adapt the functions to have a parameter that decides if money() should happen.

import moeda
b = int(input('Lemme mess with your money. How much you got?'))
print(f'Your {b} dollars are now {moeda.half(b)}.')
print(f'Boom. Now it`s {moeda.double(b)}.')
print(f'And back to {moeda.decrease(b, 10)}.')
print(f'Finally, back to you: {moeda.increase(b, 15)}.')
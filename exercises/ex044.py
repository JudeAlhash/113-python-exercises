"""
Write a script that will determine the total purchase value at a store, considering method of payment.
 If paid in full and cash, give a 10% discount. If paid in full and card give a 5% discount. Financing in 2 payments
 will get you the normal price, and financing in 3x or more installments will get you paying 20% interest.
"""

q = float(input('How many dollars worth of product are you purchasing?'))
p = str(input('''Choose method of payment:
                 [1] to pay in full with cash;
                 [2] to pay in full with card;
                 [3] to pay in 2 installments;
                 [4] to pay in 3 or more installments.\n''')).strip()
if p == '1':
    print('Oh, how nice. Since I love cash, Ill give you a 10% discount. Your purchase comes to {}, and the total is {}'.format(q, q * .90))
elif p == '2':
    print('Good. Your total would be {}, but Ill give you a 5% discount for the prompt payment. New total is {}.'.format(q, q * .95))
elif p == '3':
    print('Perfect, your purchase is of {}, and each installment will be {}.'.format(q, q / 2))
elif p == '4':
    t = float(input('In how many payments would you like to pay for this?'))
    print('Awesome, your purchase is {}, but the final amount is of {}, with each payment at {}'.format(q, q * 1.2, (q*1.2)/t))

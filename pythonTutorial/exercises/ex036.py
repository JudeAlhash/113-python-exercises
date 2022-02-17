"""Write a script that will approve a bank loan based on the following conditions:
 The monthly payments may not exceed 30% of the person's salary.
 Ask for: House value, Salary, and how many installments to finish paying the house."""

print('Welcome to Python Bank, where we will get you approved for a loan!')
salary = float(input('What is your monthly income?'))
house = float(input('And what is the value of the desired house?'))
years = float(input('How many years were you looking to pay the house in?'))

payment = house / (years * 12)
third = salary * .3

print('If you were to buy this house at {:.2f}, and intend to finish paying it in {:.2f} years, each installment '
      'would be priced at {:.2f}.'.format(house, years, payment))

if third <= payment:
    print('Sorry, you were not approved. Your salary of {:.2f} is not enough to pay for these installments. Would you '
          'like to try again?'.format(salary))
else:
    print('Congratulations, you were approved for this loan!')



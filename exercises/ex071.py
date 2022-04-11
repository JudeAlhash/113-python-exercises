# EX 071: ATM SIMULATOR
# User will inform how much will be taken out, and your script will determine how many of each bill will come out.
# $1, $10, %20 and %50 bills
v = int(input('How much money do you wish to take out from your account?'))
bill50 = v // 50
bill20 = (v % 50) // 20
bill10 = ((v % 50) % 20) // 10
bill1 = v % 10
print(f'{bill50} $50 dollar bills, {bill20} $20 dollar bills, {bill10} $10 dollar bills, {bill1} $1 dollar bills.')

# 015. Calculate total due for rented car, based on two factors: Miles driven, and days with the vehicle. The prices
# are $60 a day, and $.15 a mile.
d = int(input('How many days were you with this car?'))
m = float(input('And how many miles did you put on it?'))
t = (d * 60) + (m * .15)
print('Your total will be {:.2f} for today, sir.'.format(t))
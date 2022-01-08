# Develop a program that will ask the distance of a trip in kilometers, and then calculate the price of the ticket
# based on the distance: .50 cents a kilometer for trips that are up to 200km, and .45 cents for the trips that are
# longer than 200km.

d = int(input('How long is the trip you want to take?'))
if d < 200:
    print('Since the trip is shorter than 200km, we will be charging you .50 cents for each kilometer, which comes up '
          'to right about {} dollars.'.format(d*.5))
else:
    print('Because the trip is 200km or longer, the rate is .45 cents per km. Total is ${}, sir.'.format(d*.45))
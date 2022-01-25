#  Ask the weight of 5 different people, and then return the biggest and the smallest value.
heavy = 0
light = 0
for c in range(0, 5):
    weight = int(input('What is your weight in kg?'))
    if c == 1:
        heavy = weight
        light = weight
    else:
        if weight > heavy:
            heavy = weight
        if weight < light:
            light = weight
print('Heaviest:{}\nLightest:{}'.format(heavy, light))
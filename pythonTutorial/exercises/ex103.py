# EX 103 : Make a function with two optional parameters, that will receive a player's name and number of goals.
# optional arguments?? He made something else. String or Int Validation.
def player(name, goals):

    return name, goals


n = str(input('What is the player`s name?'))
g = str(input('How many goals has he scored?'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    n = '<unknown>'
l = []
l = player(n, g)
print(l)
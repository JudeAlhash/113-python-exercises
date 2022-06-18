# EX 078: Receive 5 values from the user onto a LIST. Then inform me of the LARGEST and the SMALLEST values, and their
# positions.

l = list()
for c in range(0, 5):
    l.append(int(input('Provide a value for me: ')))
    if c == 0:
        biggest = l[0]
        smallest = l[0]
    if l[c] >= biggest:
        biggest = l[c]
    elif l[c] <= smallest:
        smallest = l[c]
print(f' The smallest number is {smallest},and the biggest is {biggest}')

for a, b in enumerate(l):
    if b == biggest:
        print(f'The largest numbers are in the following positions: {a}')
    if b == smallest:
        print(f'The smallest numbers are in the following positions: {a}')
        
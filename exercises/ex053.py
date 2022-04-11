# PALINDROME DETECTOR
w = str(input('Type down any word.')).strip().upper().replace(' ', '')
wl = len(w)
i = ''
"""for c in range(0, wl):  # Professor's solution is more compact.
    i += w[wl - 1]
    wl -= 1"""
i = w[::-1]  # EVEN MORE OPTIMAL.
print(w, i)
if w == i:
    print('Palindrome!')
else:
    print('Not a palindrome.')

"""ALTERNATE SOLUTION

for letter in range(len(w) -1, -1, -1):
    i += w[letter]

"""

# Write a script that will receive input for N, and then show the first N number of numbers from Fibonacci sequence.
n = int(input('How many Fibonacci terms would you like to see?'))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 0
while c < n:
    if c == 0:
        print(t1)
    elif c == 1:
        print(t2)
    else:
        print(t3)
        t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1

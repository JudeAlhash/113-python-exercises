# Write a script that reads a number and breaks it down into units, tens, hundreds and thousands.

num = int(input('Write down any number.'))
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10

print('Units:{}'.format(u))
print('Tens:{}'.format(t))
print('Hundreds:{}'.format(h))
print('Thousands:{}'.format(th))




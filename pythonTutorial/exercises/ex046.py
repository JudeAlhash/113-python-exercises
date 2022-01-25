"""Counting down: Type some code that will count down from 10, pausing between each number."""
from time import sleep

for c in range(10, 0 - 1, -1):
    print(c)
    if c != 0:
        sleep(1)
print('BOOM BOOM POW!!! \nHappy new Year!!')

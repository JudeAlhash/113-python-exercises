# EX 102 : Create a program with a Factorial Function, that will receive two parameters: First: the number to be
# factored, and second: 'show' parameter to decide if the user wants to see the process or not.

def factor(a, show=False):
    """
    param a: NUMBER TO BE FACTORED.
    param show: SHOW THE FACTORING PROCESS OR NOT (boolean).
    return: FACTORED NUMBER
    """
    fact = 1
    for c in range(a, 0, -1):
        fact *= c
        if c == 1 and show==True:
            print(c, end=' = ')
        elif c != 1 and show==True:
            print(c, end=' * ')
    return fact


print(factor(4,))
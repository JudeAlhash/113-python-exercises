# EX 083 : EXPRESSION VALIDATION. Determine if said expression is Valid or Invalid based upon the number of Parenthesis
# in it.
ini = str(input('Type in a expression/formula of your choice, using parenthesis.'))
exp = []
invalid = False
for c in range(0, len(ini)):
    exp.append(ini[c])
for pos, i in enumerate(exp):
    if i == ')':
        invalid = True
        break
    elif i == '(':
        for count in range(len(exp) - 1, -1, -1):
            if exp[count] == ')':
                exp.pop(count)
                exp.remove('(')
                break
n1 = exp.count('(')
n2 = exp.count(')')
if n1 == n2 and invalid == False:
    print('VALID EXPRESSION')
else:
    print('Invalid expression!')


# Professor Solution:
L2 = []
ini2 = str(input('Give me another expression.'))
for c2 in ini2:
    if c2 == '(':
        L2.append(c2)
    elif c2 == ')':
        if len(L2) > 0:
            L2.pop()
        else:
            L2.append(c2)
            break
if len(L2) == 0:
    print('Valid')
else:
    print('INVALID')

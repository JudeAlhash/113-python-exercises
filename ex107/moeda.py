def half(a=0, cash=True):
    a = a/2
    if cash:
        return money(a)
    else:
        return a


def double(a=0, cash=True):
    a = a*2
    if cash:
        return money(a)
    else:
        return a


def decrease(a=0, percent=0, cash=True):
    a -= a*(percent/100)
    if cash:
        return money(a)
    else:
        return a


def increase(a=0, percent=0, cash=True):
    a += a*(percent/100)
    if cash:
        return money(a)
    else:
        return a


def money(a=0):
    return f'${a:.2f}'


def doAll(a=0, b=0, c=0):
    print('-' * 30)
    print('Complete Analysis'.center(30))
    print('-'*30)
    print(f'Analyzed value:   \t{money(a)}\n'
          f'Half the value:   \t{half(a)}\n'
          f'Double the value: \t{double(a)}\n'
          f'Increased by {b}%: \t{increase(a, b)}\n'
          f'Decreased by {c}%: \t{decrease(a,c)}')
    print('-' * 30)
def validateMoney(a):
    valid = False
    while not valid:
        entry = str(input(a)).replace(',', '.').strip()
        if entry.isalpha() or entry == '':
            print(f'Error: {entry} is an invalid input.')
        else:
            valid = True
            return float(entry)

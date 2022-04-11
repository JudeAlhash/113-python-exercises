# EX 106 : Make a system for the help() command.
def ajuda(com):
    help(com)


while True:
    doubt = str(input('What FUNCTION or LIBRARY do you need help with?([no] to quit)')).strip().lower()
    if doubt == 'no':
        break
    else:
        ajuda(doubt)
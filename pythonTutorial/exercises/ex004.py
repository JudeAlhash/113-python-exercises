#004 CHALLENGE : have the script tell the user as much info as possible about the input. 
n = input('Type something up.')

print('The value typed above has the {} type. Is it a number? {}. Is it a letter? {}'.format(type(n), n.isnumeric(),n.isalpha()))
# EX 097 : Write a function that will display a message, and display a line that matches th size of the message.
def message(string):
    print('-' * len(string))
    print(string)
    print('-' * len(string))


while True:
    message(str(input('Message?')))
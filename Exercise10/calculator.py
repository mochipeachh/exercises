while True:
    first_number = float(input('Hi ! please choose a number'))
    operator = input('amazing, now please choose an operator')
    second_number = float(input('great, now please choose a second number'))

    if operator == '-':
        print(first_number-second_number)
    elif operator == '+':
        print(first_number + second_number)
    elif operator == '*':
        print(first_number*second_number)
    elif operator == '/':
        print(first_number/second_number)

    continuation = input('do you want to continue yes or no?').lower()
    if continuation == 'n' or continuation == 'no':
        print('thank you for using the calculator')
        break
    elif continuation == 'yes':
        continue
    else:
        print('bad input, please try again')


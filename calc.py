f = True
while f:
    operation = input('Въведете операция: ')
    if operation == '+':
        number1 = float(input('Въведете събираемо 1: '))
        number2 = float(input('Въведете събираемо 2: '))
        print('Резултатът е ', number1 + number2)
    elif operation == '-':
        number1 = float(input('Въведете умаляемо: '))
        number2 = float(input('Въведете умалител: '))
        print('Резултатът е ', number1 - number2)
    elif operation == '**':
        number1 = float(input('Въведете основа: '))
        number2 = float(input('Въведете степен: '))
        print('Резултатът е ', number1 ** number2)
    else:
        print('Некоректна операция')

    a = input('Желаете ли да продължите(y/n): ')
    if a != 'y':
        f = False

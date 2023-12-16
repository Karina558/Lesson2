try:
    number_1 = int(input('Enter number 1: '))
    number_2 = int(input('Enter number 2: '))
    print('Sum:', number_1 + number_2)
    print('Subtraction:', number_1 - number_2)
    print('Multiplications:', number_1 * number_2)
    print('Division:', number_1 / number_2)
except Exception as e:
    print (e)

try:
    number_1 = float(input('Enter number 1: '))
    number_2 = float(input('Enter number 2: '))
    number_3 = float(input('Enter number 3: '))
    x = str(input('Enter operation (\'+\' or \'*\' or \'all\' to see Sum and Multiplications): '))
    result_1 = number_1 + number_2 + number_3
    result_2 = number_1 * number_2 * number_3
    if x == '+':
        print('\033[1;34m\tSum:\033[0m ', result_1)
    elif x == '*':
        print('\033[1;34m\tMultiplications:\033[0m ', result_2)
    elif x == 'all':
        print('\033[1;34m\tSum:\033[0m ', result_1)
        print('\033[1;34m\tMultiplications:\033[0m ', result_2)
    else:
        print('\033[91m\tError!\033[0m Please, enter \'+\' to Sum or \'*\' to Multiplicate.')
except Exception as e:
    print (e)

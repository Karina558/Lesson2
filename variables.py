try:
    diagonal_1 = float(input('Enter diagonal 1 of rhombus: '))
    diagonal_2 = float(input('Enter diagonal 1 of rhombus: '))
    result = (diagonal_1*diagonal_2)/2
    print('Square of rhombus is: ', result)
except Exception as e:
    print (e)
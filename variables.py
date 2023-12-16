try:
    width = float(input('Enter width: '))
    height = float(input('Enter height: '))
    result = width + height
    print('\tSquare is: ', result)
except Exception as e:
    print (e)
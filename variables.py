try:
    width = float(input('Enter width: '))
    height = float(input('Enter height: '))
    result = width * height
    print('Square = :', result)

except Exception as e:
    print (e)

try:
    number = int(input('Enter number: '))
    percentage = int(input('Enter percentage: '))
    result = (number * percentage) / 100
    print (result)
except Exception as e:
    print (e)

try:
    number = float(input('Enter number: '))
    percentage = float(input('Enter percentage: '))
    result = (number * percentage) / 100
    print ('\n\tPersentage of',number,'=', result,'%')
except Exception as e:
    print (e)

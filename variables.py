try:
    salary = float(input('Enter your salary: '))
    loan = float(input('Enter your credit payment: '))
    utilities = float(input('Enter your debt for utilities: '))
    result = salary - (loan + utilities)
    if result > 0:
        print('\t\033[1;34mYour net income: ', result, '\u20B4\033[0m')
    elif result < 0:
        print('\t\033[91mYour losess: ', result, '\u20B4\033[0m')
except Exception as e:
    print (e)
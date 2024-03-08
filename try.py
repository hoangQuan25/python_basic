num1 = int(input('enter the 1st number'))
num2 = int(input('enter the 2nd number'))

try:
    res = num1/ num2
    print(res)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
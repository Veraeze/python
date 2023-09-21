count = 1
number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
if number1 == 1 or number1 == 2 and number2 == 1 or number2 == 2:
    total = number1 + number2
    count = 1
    fail = count - 1
else:
    while number1 != 1 or number1 != 2 and number2 != 1 or number2 != 2:
        count += 1
        number1 = int(input('Enter first integer: '))
        number2 = int(input('Enter second integer: '))
        if number1 == 1 or number1 == 2 and number2 == 1 or number2 == 2:
            break
total = number1 + number2
fail = count - 1
print(f'''The sum of {number1} and {number2} is {total}, 
the number of passes is {count} and the number of failures is {fail}''')


number_one = int(input('Enter first number: '))
number_two = int(input('Enter second number: '))
number_three = int(input('Enter third number: '))

if number_three < number_one > number_two:
    largest = number_one
elif number_three > number_one < number_two:
    smallest = number_one
else:
    middle = number_one

if number_one < number_two > number_three:
    largest = number_two
elif number_one > number_two < number_three:
    smallest = number_two
else:
    middle = number_two

if number_two < number_three > number_one:
    largest = number_three
elif number_two > number_three < number_one:
    smallest = number_three
else:
    middle = number_three

print(smallest, '\n', middle, '\n', largest)






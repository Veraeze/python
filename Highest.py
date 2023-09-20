number_one = int(input("Enter first number"))
number_two = int(input("Enter second number"))
number_three = int(input("Enter third number"))

if number_three < number_one > number_two:
    highest = number_one

if number_one < number_two > number_three:
    highest = number_two

if number_two < number_three > number_one:
    highest = number_three

print(highest)

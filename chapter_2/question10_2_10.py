number_one = int(input("Enter first integer: "))
number_two = int(input("Enter second integer: "))
number_three = int(input("Enter third integer: "))

sum = number_one + number_two + number_three
average = (number_one + number_two + number_three) / 3
product = number_one * number_two * number_three

if number_three < number_one > number_two:
    largest = number_one
elif number_three > number_one < number_two:
    smallest = number_one

if number_one < number_two > number_three:
    largest = number_two
elif number_one > number_two < number_three:
    smallest = number_two

if number_two < number_three > number_one:
    largest = number_three
elif number_two > number_three < number_one:
    smallest = number_three

print('The sum of numbers is', sum)
print('The average of numbers is', average)
print('The product of numbers is', product)
print('The smallest number is', smallest)
print('The largest number is', largest)





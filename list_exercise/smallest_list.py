numbers = [15, 20, 25, 20, 10, 5]

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print(f"The smallest of the list of numbers is {smallest}")

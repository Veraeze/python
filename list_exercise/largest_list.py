numbers = [15, 20, 25, 20, 10, 5]

largest = 0
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest of the list of numbers is {largest}")

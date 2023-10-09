numbers = [15, 20, 25, 20, 10, 5]
new = []
for number in range(len(numbers)):
    if numbers[number] not in new:
        new.append(numbers[number])
print(new)

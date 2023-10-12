numbers = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
print("Original list :",numbers)
for i in range(0, len(numbers)):
     for j in range(i+1, len(numbers)):
        if numbers[i] >= numbers[j]:
            numbers[i], numbers[j] =numbers[j], numbers[i]
print('arranged list:', numbers)

if len(numbers) % 2 == 0:
    mid1 = len(numbers) // 2
    mid2 = mid1 - 1
    median = (numbers[mid2] + numbers[mid1]) / 2
else:
    mid = (len(numbers) // 2) + 1
    median = numbers[mid]

sum = 0
for m in numbers:
    sum = sum + m
mean = sum / len(numbers)

print(median)
print(mean)


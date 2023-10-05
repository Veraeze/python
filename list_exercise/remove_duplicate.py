numbers = [15, 20, 25, 20, 10, 5]
new = []
for number in range(len(numbers)):
    if numbers[number] not in new:
        new.append(numbers[number])
print(new)





























# high = 0
# duplicate = 0
# for number in numbers:
#     count = 0
#     for integer in numbers:
#         if number == integer:
#             count += 1
#     if count > high:
#         high = count
#         duplicate = number
# numbers.remove(duplicate)
# print(numbers)

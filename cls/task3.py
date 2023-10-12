even_numbers = []
for i in range(2, 51, 2):
    even_numbers.append(i)
print(even_numbers)
average = sum(even_numbers) / len(even_numbers)
print(average)


sums = 0
count = 0
even = 0
while even < 50:
    even += 2
    count += 1
    sums += even
    average = sums / count
print(f'{average:.2f}')

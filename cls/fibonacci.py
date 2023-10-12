# while loop
first = 0
second = 1
sums = first + second
while first < 50:
    print(first, end=' ')
    first = second
    second = sums
    sums = first + second

# for loop
first = 0
second = 1
sumz = first + second
for i in range(0, 51):
    if first>50:
        break
    print(first, end=' ')
    first = second
    second = sumz
    sumz = first + second



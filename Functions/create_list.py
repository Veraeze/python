numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

numbers2 = list(range(1, 21))
print(numbers2)


def even_check(n):
    ans = 0
    if n % 2 == 0:
        ans = n
    return ans


even_list = filter(even_check, numbers)
print(list(even_list))

result = [i for i in range(1, 11) if i % 2 == 0]
print(result)


def odd_list(number_list):
    return list(filter(lambda x: x % 2 == 1, number_list))

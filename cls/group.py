def create_list(number_list: list):
    for i in range(1, 21):
        numbers.append(i)
    return numbers


def create_list_odd(number_list: list):
    for i in range(1, 21, 2):
        numbers.append(i)
    return numbers


def create_list_double(number_list: list):
    for i in range(1, 21, 2):
        numbers.append(i * 2)
    return numbers


def create_list_zero(number_list: list):
    count = 4
    for i in range(1, 21, 2):
        numbers.append(i * 2)
    for index in numbers:
        numbers[count] = 0
        count += 1
        if count == 8:
            break
    return numbers


numbers = []
counts = 4
for number in range(1, 21, 2):
    numbers.append(number * 2)
numbers[4:7] = [0] * 4
print(numbers)

 
def concanate(list1, list2):
    return [x+y for x, y in zip(list1, list2)]


# numbers2 = list(range(1, 11))
# print(numbers2)


# numbers2 = [odd for odd in range(1, 21) if odd % 2 != 0]
# print(numbers2)

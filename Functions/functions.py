def rate(percentage: int) -> int:
    if percentage < 50:
        return percentage * 160 + 5000
    elif percentage <= 59:
        return percentage * 200 + 5000
    elif percentage <= 69:
        return percentage * 250 + 5000
    else:
        return percentage * 500 + 5000


def copy(copies: int) -> int:
    if 0 < copies <= 4:
        return 2000
    elif copies <= 9:
        return 1800
    elif copies <= 29:
        return 1600
    elif copies <= 49:
        return 1500
    elif copies <= 99:
        return 1300
    elif copies <= 199:
        return 1200
    elif copies <= 499:
        return 1100
    else:
        return 1000


def is_even(integer: int) -> bool:
    if integer % 2 == 0:
        return True
    else:
        return False


def is_prime_number(integer: int) -> bool:
    result = 0
    count = 1
    while count <= integer:
        if integer % count == 0:
            result += 1
        count += 1
    if result == 2:
        return True
    else:
        return False


def subtract(first_number: int, second_number: int) -> int:
    if first_number > second_number:
        return first_number - second_number
    else:
        return second_number - first_number


def divide(first_integer: int, second_integer: int) -> float:
    result = first_integer / second_integer
    quotient = round(result, 2)
    if second_integer != 0:
        return quotient
    else:
        return 0


def factor_of(integer: int) -> int:
    factor = is_prime_number(integer)
    if factor > 0:
        return factor
    else:
        return 0


def is_square(integer: int) -> bool:
    for count in range(integer):
        if integer / count == count:
            return True
    return False


def is_palindrome(integer: int) -> bool:
    first = integer / 10000
    last = integer % 10
    if first == last:
        return True
    else:
        return False


def factorial_of(integer: int) -> int:
    factorial = 1
    is_negative_number = integer < 0
    if is_negative_number:
        return 0
    count = integer
    while count >= 1:
        factorial *= count
        count -= 1
    return factorial


def raise_power(base: int, power: int) -> int:
    result = 1
    for i in range(power):
        result *= base
    return result


def multiply(*numbers: int) -> int:
    product = 1
    for i in numbers:
        product *= i
    return product


def average(*integers) -> float:
    total = 0
    for scores in integers:
        total += scores
    return total / len(integers)


def largest_element(integers: int) -> int:
    largest = 0
    for number in integers:
        if number > largest:
            largest = number
    return largest


def reverse_list(integers):
    rev_integers = []
    for i in reversed(integers):
        rev_integers.append(i)
    return rev_integers


def check_element(integer: int, integers) -> bool:
    for number in integers:
        if number == integer:
            return True
    return False


def odd_positions(integers):
    odd = []
    for number in range(integers[0], len(integers), 2):
        odd.append(number)
    return odd


def even_positions(integers):
    even = []
    for number in range(integers[1], len(integers) + 1, 2):
        even.append(number)
    return even


def running_total(integers):
    total = 0
    result = []
    for number in integers:
        total += number
        result.append(total)
    return result


def word_palindrome(word: str) -> bool:
    for letter in word:
        if word[0] == word[len(word)-1]:
            return True
    return False


def for_sum(integers) -> int:
    add = 0
    for number in integers:
        add += number
    return add


def while_sum(integers) -> int:
    add = 0
    count = 0
    while count < len(integers):
        for number in integers:
            add += number
            count += 1
    return add


def concatenate_lists(letters, integers):
    first_input = []
    second_input = []
    for letter in letters:
        first_input.append(letter)
    for integer in integers:
        second_input.append(integer)
    return first_input + second_input


def triple(numbers):
    new = []
    for number in numbers:
        new.append(number**3)
    return new
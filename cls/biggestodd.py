def biggest_odd(numbers: str):
    return max([i for i in numbers if int(i) % 2 == 1])

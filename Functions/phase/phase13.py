def concatenate_lists(letters: list):
    inputs = " "
    for letter in letters:
        inputs = inputs + letter
    return inputs


print(concatenate_lists([1, 2, 3, 4]))
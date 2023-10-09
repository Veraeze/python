def reverse_tuple(*tuple1) -> tuple:
    rev_integers = ()
    for i in reversed(tuple1):
        rev_integers = rev_integers + (i, )
    return rev_integers


def nested_tuple(*tuple2):
    numbers = ()
    integers = ()
    tuple2[0] = numbers
    tuple2[1] = integers
    return numbers.index(numbers)


def swap_tuple(*tuple3) -> tuple:
    element_1 = tuple3[len(tuple3) - 1]
    element_2 = tuple3[0]
    return element_1, element_2


def sort_tuple(*tuple4):
    elements_1 = ()
    for unit in range(len(tuple4) // 2):
        elements_1 += (tuple4[unit], )

    elements_2 = ()
    for units in range((len(tuple4) // 2), len(tuple4)):
        elements_2 += (tuple4[units], )

    new_tuple = ()
    for count in range(len(elements_2)):
        new_tuple += (elements_2[count], ) + (elements_1[count], )

    return new_tuple


def return_duplicate(*tuple5):
    duplicate = ()
    for number in tuple5:
        if tuple5.count(number) > 1:
            duplicate = duplicate + (number, )

    new_duplicate = ()
    for number in range(len(duplicate)):
        if duplicate[number] not in new_duplicate:
            new_duplicate = new_duplicate + (duplicate[number], )

    rev_duplicate = ()
    for number in reversed(new_duplicate):
        rev_duplicate = rev_duplicate + (number, )

    return rev_duplicate

from Functions import functions
from Functions import tuples


def reverse_tuple(*tuple1) -> tuple:
    rev_integers = ()
    for i in reversed(tuple1):
        rev_integers = rev_integers + (i, )
    return rev_integers


def nested_tuple(*tuple2):
    numbers = ()
    integers = ()

    for index, value in enumerate(tuple2):
        if index == 1:
            numbers += index - 1,
            numbers += value[1],

        if index == 2:
            integers += index - 1,
            integers += value[2],

    return numbers, integers


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
    for i in reversed(new_duplicate):
        rev_duplicate = rev_duplicate + (i, )

    return rev_duplicate


def my_sort_method(list1, rev=False):
    for i in range(0, len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
            if list1[i] < list1[j] and rev == True:
                list1[i], list1[j] = list1[j], list1[i]
    return list1

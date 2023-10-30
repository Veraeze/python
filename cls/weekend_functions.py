from turtle import pd


def list_to_dictionary(inputs: list):
    output = {}
    for i in inputs:
        key = i[0]
        output.update({key: i})
    return output


def two_list_to_dictionary(input1: list, input2: list):
    sam_output = {}
    count = 0
    for value in input1:
        element = input2[count]
        sam_output.update({value: element})
        count += 1
    return sam_output


def largest_minus_smallest(list1: list):
    return max(list1)-min(list1)


def greater_than_value(sam_list: list, k: int):
    new_list = []
    counts = 0
    new = [number for number in range(len(sam_list)) if sam_list[number] not in new_list]
    for i in new:
        if sam_list.count(new[counts]) > k:
            new_list.append(new[counts])
        counts += 1
    return new_list


def empty_string(samp_input: list):
    return [string1 for string1 in samp_input if len(string1) > 0]


def split_list(input0: list):
    ouput0 = [input0[i] for i in range(len(input0)//2)]
    output1 = [j for j in input0 if j not in ouput0]
    return f'{ouput0}, {output1}'


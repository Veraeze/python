import Functions.functions


def student_ages(student_age: dict, studentname: str, new_age=0):
    student_name = studentname.lower()
    if student_name not in student_age:
        new_age = int(input("name not in dictionary, please enter age: "))
        student_age.update({student_name: new_age})
        return f"Hi, {student_name}, you are {student_age[student_name]} years old. \n{student_age}"
    else:
        print(f"Hi, {student_name}, you are {student_age[student_name]} years old.")
        return f"Hi, {student_name}, you are {student_age[student_name]} years old."


def sum_nested_list(integers: list):
    total = 0
    for i in integers:
        for j in i:
            total += j
    return total


def sum_nested_list2(integers: list):
    a, b = integers
    total = sum(a + b)
    return total


def even_integer_list():
    sample_list = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]
    result = Functions.functions.remove_duplicate_array([i for i in sample_list if i % 2 == 0])
    return result

def list_to_dictionary(input_list: list):
    output_dict = {}
    for i in input_list:
        key = i[0]
        output_dict.update({key: i})
    if key in output_dict:
        key2 = key.capitalize()
        output_dict.update({key2: i})
    return output_dict

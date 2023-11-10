# # writing to a file
# with open("demo.txt", mode='w') as file:
#     file.write("my name is vera\n")
#     file.write("im trying to create a file in python\n")
#     file.write("lets see how well this works\n")
#
#
# # appending to a file
# with open("demo.txt", mode='a') as file:
#     file.write("this is to append to demo")
#
# # reading from a file
# with open("demo.txt", mode='r') as file:
#     print(f'{"First":<10}{"Second":<10}{"Third":>10}')
#     for line in file:
#         first, second, third, *four = line.split()
#         print(f'{first:<10}{second:<10}{ third:>10}')
#


# # exceptions in a code
# try:
#     age = int(input("Enter your age: "))
#     result = 10/age
#     print(result)
# except (ZeroDivisionError, ValueError):
#     print("Your age cannot be zero and cannot be divided by a string literal")
# finally:
#     print("code after the exception will still run due to the finally keyword")


# # raising exception in a function
# def age_check(n):
#     if n <= 0:
#         raise ValueError("age cannot be less than or equal to zero")
#     return f'you are {n} years old'
#
#
# print(age_check(-2))


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print(f"drawing from point {self.a} to point {self.b}")


point1 = Point(1, 2)
point2 = Point(5, 6)
point1.draw()
point2.draw()



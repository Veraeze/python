integer1 = int(input("Enter first integer: "))
integer2 = int(input("Enter second integer: "))
integer3 = int(input("Enter third integer: "))
integer4 = int(input("Enter fourth integer: "))

even_number = 0
odd_number = 0

if integer1 % 2 == 0:
    even_number = integer1
elif integer1 % 2 != 0:
    odd_number = integer1

if integer2 % 2 == 0:
    even_number = even_number + integer2
elif integer2 % 2 != 0:
    odd_number = odd_number + integer2

if integer3 % 2 == 0:
    even_number = even_number + integer3
elif integer3 % 2 != 0:
    odd_number = odd_number + integer3

if integer4 % 2 == 0:
    even_number = even_number + integer4
elif integer4 % 2 != 0:
    odd_number = odd_number + integer4


print(even_number)
print(odd_number)

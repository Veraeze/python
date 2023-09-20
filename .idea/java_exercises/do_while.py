first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

sum = first_number + second_number

print('The sum is', sum)

while True:
    answer = int(input("Do you want to perform this operation again? If yes press 1, if no press 0: "))
    if answer == 1:
        print('The sum is', sum)
    if answer == 0:
        break


integer = int(input('Enter 5 digit integer: '))

first = integer // 10000
remainder = integer % 10000

second = remainder // 1000
remainder = integer % 1000

third = remainder // 100
remainder = integer % 100

fourth = remainder // 10
remainder = integer % 10

fifth = remainder

print(first, '\t', second, '\t', third, '\t', fourth, '\t', fifth)
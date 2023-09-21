# left align
print('''number \t square \t cube''')
number = 0
while number <= 5:
    print(f'{number}   \t  {number**2}      \t {number**3}')
    number += 1

# right align
print('''number \t square \t cube''')
number = 0
while number <= 5:
    print(f'    {number}   \t  {number**2}      \t {number**3}')
    number += 1



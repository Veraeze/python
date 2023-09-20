zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5

zero_2 = zero ** 2
one_2 = one ** 2
two_2 = two ** 2
three_2 = three ** 2
four_2 = four ** 2
five_2 = five ** 2

zero_3 = zero ** 3
one_3 = one ** 3
two_3 = two ** 3
three_3 = three ** 3
four_3 = four ** 3
five_3 = five ** 3

# left align
print(f'''number \t square \tcube
{zero}   \t  {zero_2}   \t    {zero_3}
{one}   \t  {one_2}   \t    {one_3}
{two}   \t  {two_2}   \t    {two_3}
{three}   \t  {three_2}   \t    {three_3}
{four}   \t  {four_2}   \t    {four_3}
{five}   \t  {five_2}   \t    {five_3}''')

# right align
print('number \t square \tcube')
print('\t',  zero, '  \t ', zero_2, '  \t  ', zero_3)
print('\t', one, '  \t ', one_2, '  \t  ', one_3)
print('\t', two, '  \t ', two_2, '  \t  ', two_3)
print('\t', three, '  \t ', three_2, '  \t  ', three_3)
print('\t', four, '  \t ', four_2, '  \t  ', four_3)
print('\t', five, '  \t ', five_2, '  \t  ', five_3)


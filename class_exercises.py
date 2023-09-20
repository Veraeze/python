# print(type(2))
# print(type(2.1))
# print(type(True))
# print(type('david'))
#
# print(2)
# print(2.1)
# print(True)
# print('david')
#
# # foundamental data types
# print(10 + 4)
# print(10 - 4)
# print(10 * 4)
# print(10 / 4)
# print(10 // 4)
# print(10 % 4)
#
# name = 'alphred'
# print(len(name))

# password = input("Enter your password: ")
# print(len(password) * '*')

# number = 2 ** 3
# print(number)

# message ='it\'s \tpy\nthon'
# print(message)

# print('The answer is', 3+4+5)

# message = '''             eifjkdeigdijrgierjgnejgiejgsgrjebzvrevzudlfifjvnerzdfvkjbn
#              rehdufzvhgbgrgnbfijdhrgrejighjernrhgufdnergiegrtnnwmefnwji
#              hfikfeihfuiesihkiferhfhrejniuijefieufhuigrjguifdyuikrgnuig
#              hteiurifhfuerijgrfuighngreuruijfgneiuegnjrejjhtnregrt4nojh
#              hi9ujernritiotjrhufjrnergbfugrrygrehrgiureehgirjrgbreugsko
#              rhghkrngejegrskgneklgiggijrnknkfdnkofodj.lkgeneogjoefgmrgr
#              jtjoflknnkfdn'''
# print(message)
#
# num1 = '1'
# num2 = str(2)
# print(num1 + num2)

# message1 = 'hello'
# message2 = 'welcome'
# message3 = 'explorers'
# msg3 = f'{message1} {message2} {message3}'
# print(msg3)
# msg = f'{message1 + ", how are you"}\n{message2}\n{message3}'
# print(msg)
# msg2 = f'{message1 + ", how are you"}\t{message2}\t{message3}'
# print(msg2)
# print(message1 + ", how are you " + message2 + ' ' + message3, end='\t')


# age = int(input("Enter an age: "))
# if age < 18:
#     print("you're not eligible to enter our club...")
# if 18 <= age <= 65:
#     print("you're eligible tp enter our club...")
# if age > 65:
#     print("stay home...")


age = int(input("Enter an age: "))
if age < 18:
    print("you're not eligible to enter our club...")
elif 18 <= age <= 65:
    print("you're eligible tp enter our club...")
else:
    print('stay home...')



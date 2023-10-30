word = input("Enter string: ")
n = int(input("Enter copies: "))
if len(word) >= 2:
    for letter in range(len(word)-(len(word) - 2)):
        result = (word[letter-1] + word[letter]) * n
    print(result)
else:
    print(word * n)

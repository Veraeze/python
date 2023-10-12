word = input("Enter string: ")
n = int(input("Enter copies: "))
remain = len(word) - 2
if len(word) >= 2:
    for letter in range(len(word)-remain):
        result = (word[letter-1] + word[letter]) * n
    print(result)
else:
    result = word * n
    print(result)

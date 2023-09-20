# rating = input('Enter an integer rating between 1 and 10')
# what's wrong with the code is that the rating would be a string rather than an integer
# casting the input using int would transform the rating from a string to an integer
# hence, the correct code should be;

rating = int(input('Enter an integer rating between 1 and 10: '))

print(rating)

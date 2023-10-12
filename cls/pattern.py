for row in range(6):
    for line in range(row):
        print('*', end=' ')
    print()
for row in range(4, 0, -1):
    for line in range(1, row + 1):
        print('*', end=' ')
    print()
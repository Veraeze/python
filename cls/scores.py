# score = 0
# count = 0
# while True:
#     scores = int(input('Enter score(press -1 to stop): '))
#     if scores == -1:
#         break
#     score += scores
#     count += 1
# print(f'''The average of the scores is {score / count:.2f}''')

score = 0
count = 0
scores = int(input('Enter a score(press -1 to stop): '))
while scores != -1:
    score += scores
    count += 1
    scores = int(input('Enter score(press -1 to stop): '))
print(f'''The average of the scores is {score / count:.2f}''')
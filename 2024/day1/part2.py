
with open('input.txt', 'r') as file:
    left_column = []
    right_column = []
    for line in file:
        left, right = map(int, line.split())
        left_column.append(left)
        right_column.append(right)


score = 0
for number in left_column:
    occurrences = right_column.count(number)
    score += number * occurrences


print(score)

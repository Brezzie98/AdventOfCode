

with open('input.txt', 'r') as file:
    left_col = []
    right_col = []
    for line in file:
        left, right = map(int, line.split())
        left_col.append(left)
        right_col.append(right)

left_col.sort()
right_col.sort()

count = 0
for ii in range(len(left_col)):
    diff = abs(left_col[ii] - right_col[ii])
    count += diff


print(count)



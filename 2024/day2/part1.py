

def is_safe(report):
    diffs = []
    for i in range(len(report) - 1):
        diffs.append(report[i+1] - report[i])

    valid_diffs = True
    for diff in diffs:
        if not (-3 <= diff <= -1 or 1 <= diff <= 3):
            valid_diffs = False
            break

    all_increasing = True
    all_decreasing = True
    for diff in diffs:
        if diff <= 0:
            all_increasing = False
        if diff >= 0:
            all_decreasing = False

    return valid_diffs and (all_increasing or all_decreasing)


with open('input.txt', 'r') as file:
    reports = []
    for line in file:
        levels = line.split()
        int_levels = []
        for level in levels:
            int_levels.append(int(level))
        reports.append(int_levels)

safe_count = 0
for report in reports:
    if is_safe(report):
        safe_count += 1

print(safe_count)
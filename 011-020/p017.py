
ones = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
teens = {'0': 0, '1': 3, '2': 3, '3': 3, '4': 4, '5': 3, '6': 4, '7': 4, '8': 3, '9': 4}
tens = {'0': 0, '1': 3, '2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}


total_count = 0
for i in range(1, 1001):
    count = 0
    i = str(i)
    if len(i) >= 1:
        count += ones[i[-1]]
    if len(i) >= 2:
        if i[-2] == 1:
            count += teens[i[-2]]
        else:
            count += tens[i[-2]]
    if len(i) >= 3:
        count += ones[i[-3]] + len('hundred')
        if (i[-1] != '0' or i[-2] != '0') and i[-3] != '0':
            count += 3
    if len(i) >= 4:
        count += ones[i[-4]] + len('thousand')
        if (i[-1] != '0' or i[-2] != '0') and i[-3] != '0':
            count += 3
    total_count += count

print(total_count)

l = [2, 7, 8, 13, 1, 98, 44, 63, 86]
min_num, max_num = l[0], l[0]
for num in l:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print(f"The max - {max_num} and the min - {min_num}")

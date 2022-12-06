l = [24, 4, 5, 2, 6, 36]

for i in range(0, len(l), 1):
    swapped = 0
    for j in range(i, len(l), 1):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
        swapped = 1

    if swapped == 0:
        break
print(l)

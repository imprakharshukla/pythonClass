li = []
n = int(input("Please enter the number of elements \n"))
i = 0
while i < n:
    j = int(input("Enter number \n"))
    li.append(j)
    i += 1
s = 0
p = 1
for i in li:
    s += i
    p *= i

print(f"Average - {float(s / len(li))}")
print(f"Product - {p}")

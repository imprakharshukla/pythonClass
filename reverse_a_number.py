inp = (input("Please enter a number \n"))
n = int(inp)
temp = n
rev = 0
k = len(inp) - 1
while temp != 0:
    rev += int(temp%10 * pow(10, k))
    k -= 1
    temp = int(temp / 10)
print(rev)
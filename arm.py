n = input("Enter a number \n")
l = len(n)
num = int(n)
product = 0
for i in range(0, l, 1):
    digit = int(num % 10)
    num = int(num / 10)
    product = product + pow(digit, l)

if product == int(n):
    print("Arm. Number")
else:
    print("Not Arm. Number")



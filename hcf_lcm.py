a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

HCF = 1

for i in range(2, a + 1):
    if a % i == 0 and b % i == 0:
        HCF = i

LCM = int((a * b) / HCF)

print(f"LCM - {LCM}, HCF - {HCF}")

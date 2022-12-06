n = int(input("Enter the required number of fib series terms \n"))
a = 0
b = 1
print(a)
print(b)
for i in range(0, n):
    c = a + b
    print(c)
    a = b
    b = c

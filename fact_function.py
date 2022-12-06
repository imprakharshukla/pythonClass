# def factorial(n):
#     fac = 1
#     for i in range(1, n, 1):
#         fac *= i
#     return fac


def factorial(n = 8):
    fac = 1
    for i in range(1, n-1, 1):
        fac *= i
    return fac


print(factorial())
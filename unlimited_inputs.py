numbers = []


def average(numbers):
    s = 0
    for i in numbers:
        s += i
    return s / len(numbers)


def product(numbers):
    prod = 1;
    for i in numbers:
        prod *= i
    return prod


while 1:
    num = input("Please enter a number or press e to exit: ")
    if num == 'e':
        print(f"Product - {product(numbers)}")
        print(f"Average - {average(numbers)}")
        break
    else:
        num = int(num)
        numbers.append(num)

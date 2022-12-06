st = input("Please input a string \n")
rev = (st[::-1])
if st == rev:
    print("The string is symmetric")
else:
    print("The string is not symmetric")
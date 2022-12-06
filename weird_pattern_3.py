num = input("Please enter the pattern string \n")

for n in num:
    for i in range(0, int(n)):
        print("*", end="")
    print("")

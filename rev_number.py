# The value of n in the above program has to store somewhere so I have taken m variable in place of n in a func def.

def revNumber(m):
    k = len(str(m))
    rev = 0
    while m != 0:
        dig = int(m % 10)
        print(f"{dig} k-{k}")
        rev = int(dig * pow(10, k))
        k+=1
        m/=10

    return rev


revNumber(1023)
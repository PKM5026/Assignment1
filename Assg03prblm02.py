def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def twins(start, end):
    for i in range(start, end):
        j = i + 2
        if (prime(i) and prime(j)):
            print("{:d} and {:d}". format(i,j))

twins(2, 20)

from math import sqrt


def MinDivisor(n):
    s = int(sqrt(n))
    for i in range(2, s + 1):
        if (n % i == 0):
            return (i)
    return (n)


a = int(input())
print(MinDivisor(a))

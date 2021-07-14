from math import sqrt


def isPrime(n):
    s = int(sqrt(n))
    for i in range(2, s + 1):
        if (n % i == 0):
            return ("NO")
    return ("YES")


a = int(input())
print(isPrime(a))

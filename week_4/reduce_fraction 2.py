def gcd(a, b):
    if (b == 0):
        return (a)
    if (b == 1):
        return 1
    return gcd(b, a % b)


def ReduceFraction(p, q):
    d = gcd(p, q)
    return (p // d, q // d)


p = int(input())
q = int(input())
print(*ReduceFraction(p, q))

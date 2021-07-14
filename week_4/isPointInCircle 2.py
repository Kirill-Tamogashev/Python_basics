from math import pow


def IsPointInCircle(x, y, xc, yc, r):
    return pow(x - xc, 2) + pow(y - yc, 2) <= pow(r, 2)


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
print(IsPointInCircle(a, b, c, d, e) * "YES" or "NO")

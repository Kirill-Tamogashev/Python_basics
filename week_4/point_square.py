def isPointInSquare(x, y):
    return (-1 <= x <= 1 and -1 <= y <= 1)

a = float(input())
b = float(input())
print(isPointInSquare(a, b) * "YES" or "NO")

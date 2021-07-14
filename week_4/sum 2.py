def Sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return (Sum(a - 1, b + 1))


a = int(input())
b = int(input())
print(Sum(a, b))

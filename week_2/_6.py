a = int(input())
b = int(input())
c = int(input())
if a >= b >= c:
    a, b, c = c, b, a
elif a >= c >= b:
    a, b, c = b, c, a
elif b >= a >= c:
    a, b, c = c, a, b
elif b >= c >= a:
    a, b, c = a, c, b
elif c >= b >= a:
    a, b, c = a, b, c
elif c >= a >= b:
    a, b, c = b, a, c
print(a, b, c)

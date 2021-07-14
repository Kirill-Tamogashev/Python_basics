n = int(input())
i = 1
a = []
while i ** 2 <= n:
    a.append(i ** 2)
    i += 1
print(*a)

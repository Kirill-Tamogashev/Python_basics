n = int(input())
seqSum = 0
i = 1
while i <= n:
    seqSum += 1 / (i ** 2)
    i += 1
print(seqSum)

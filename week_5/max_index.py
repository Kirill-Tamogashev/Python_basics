lst = list(map(int, input().split()))
index = 0
maxx = lst[index]
for i in range(1, len(lst)):
    if lst[i] >= maxx:
        maxx = lst[i]
        index = i
print(maxx, index, sep=' ')

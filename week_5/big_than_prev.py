lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    if lst[i - 1] < lst[i]:
        print(lst[i], end=' ')

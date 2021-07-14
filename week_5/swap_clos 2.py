lst = list(map(int, input().split()))
for i in range(1, len(lst), 2):
    tmp = lst[i - 1]
    lst[i - 1] = lst[i]
    lst[i] = tmp
print(*lst)

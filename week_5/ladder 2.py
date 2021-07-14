num = int(input())
lst = []
for i in range(1, num + 1):
    for j in range(1, i + 1):
        lst.append(j)
    print(*lst, sep='')
    lst.clear()

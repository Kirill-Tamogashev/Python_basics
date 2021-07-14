n = int(input())
lst = list(map(int, input().split()))
num = int(input())
lst_abs = []
for i in range(n):
    lst_abs.append((abs(num - lst[i]), lst[i]))
print(min(lst_abs)[1])

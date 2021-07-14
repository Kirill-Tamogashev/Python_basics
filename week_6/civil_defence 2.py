def SortList(a):
    # создаем и сортируем пары
    len_a = len(a)
    a_ext = []
    for i in range(len_a):
        a_ext.append((a[i], i + 1))
    a_ext.sort()
    return a_ext


def FindMyShelter(a, b):
    # мэтчим отсортированные списки и составляем список мэтчей
    len_a = len(a)
    len_b = len(b)
    s = 0
    match = []
    for i in range(len_a):
        a_i_0 = a[i][0]
        for j in range(s, len_b):
            if j == len_b - 1:
                match.append((a[i][1], b[j][1]))
            else:
                if abs(a_i_0 - b[j][0]) <= abs(a_i_0 - b[j + 1][0]):
                    match.append((a[i][1], b[j][1]))
                    s = j
                    break
    return match


def Info(a):
    # выводим строку с ответом
    a.sort()
    len_a = len(a)
    for i in range(len_a):
        print(a[i][1], end=' ')


n = int(input())
settlement = list(map(int, input().split()))
m = int(input())
shelter = list(map(int, input().split()))

Info(FindMyShelter(SortList(settlement), SortList(shelter)))

def P(n):
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n]
    g = list()
    for j in range(len(n)):
        p = n[j]
        q = n[:j] + n[j + 1:]
        for elem in P(q):
            g.append([p] + elem)
    return g


n = list(input())
for elem in P(n):
    print(''.join(elem))

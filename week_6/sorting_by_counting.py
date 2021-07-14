def CountSort(A):
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    A[:] = []
    for number in range(scope):
        A += [number] * C[number]
    return A


print(*CountSort(list(map(int, input().split()))))

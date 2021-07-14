n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, list(input()))))

matrix_max = []
for i in range(n + 1):
    a = []
    for j in range(n + 1):
        a.append(0)
    matrix_max.append(a)

matrix_max[0][0] = matrix[0][0]
for i in range(1, n):
    matrix_max[0][i] = matrix_max[0][i - 1] + matrix[0][i]
for i in range(1, n):
    matrix_max[i][0] = matrix_max[i - 1][0] + matrix[i][0]

for i in range(1,  n):
    for j in range(1, n):
        if matrix_max[i - 1][j] > matrix_max[i][j - 1]:
            matrix_max[i][j] = matrix_max[i][j - 1] + matrix[i][j]
        else:
            matrix_max[i][j] = matrix_max[i - 1][j] + matrix[i][j]


def way(i, j):
    if i == j == 0:
        matrix_max[i][j] = "#"
        return n

    if i == 0 and j != 0:
        matrix_max[i][j] = "#"
        return way(i, j - 1)
    elif j == 0 and i != 0:
        matrix_max[i][j] = "#"
        return way(i - 1, j)
    if i > 0 and j > 0:
        if matrix_max[i - 1][j] > matrix_max[i][j - 1]:
            matrix_max[i][j] = "#"
            return way(i, j - 1)
        else:
            matrix_max[i][j] = "#"
            return way(i - 1, j)
    return 0


way(n - 1, n - 1)
for i in range(n):
    for j in range(n):
        if matrix_max[i][j] != "#":
            matrix_max[i][j] = "-"

for i in range(n):
    for j in range(n):
        print(matrix_max[i][j], end='')
    print()

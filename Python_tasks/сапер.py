n = list(map(int, input().split()))
li = []
for i in range(n[2]):
   kr = list(map(int, input().split()))
   li.append(kr)

matrix = []
for i in range(n[0] + 2):
    a = []
    for j in range(n[1] + 2):
        a.append(0)
    matrix.append(a)

for j in range(len(li)):
    for p in range(n[0] + 1):
        for q in range(n[1] + 1):
            if p + 1 == li[j][0] and q + 1== li[j][1]:
                matrix[p + 1][q + 1] = "*"


for p in range(1, n[0] + 1): #1
    for q in range(1, n[1] + 1):
        if matrix[p - 1][q - 1] == "*" and matrix[p][q] != "*":
            matrix[p][q] += 1

for p in range(1, n[0] + 1):
    for q in range(1, n[1] + 1):
        if matrix[p - 1][q] == "*" and matrix[p][q] != "*":
            matrix[p][q] += 1

for p in range(1, n[0] + 1):
    for q in range(1, n[1] + 1):
        if matrix[p - 1][q + 1] == "*" and matrix[p][q] != "*":  #####
            matrix[p][q] += 1

for p in range(1, n[0] + 1):
    for q in range(1, n[1] + 1):
        if matrix[p][q - 1] == "*" and matrix[p][q] != "*":
            matrix[p][q] += 1

for p in range(1, n[0] + 1):
    for q in range(1, n[1] + 1):
        if matrix[p][q + 1] == "*" and matrix[p][q] != "*":
            matrix[p][q] += 1

for p in range(1, n[0] + 1):
    for q in range(1, n[1] + 1):
        if matrix[p + 1][q - 1] == "*" and matrix[p][q] != "*":
            matrix[p][q] += 1

for p in range(1, n[0] + 1):
    for q in range(1, n[1] + 1):
        if matrix[p + 1][q] == "*" and matrix[p][q] != "*":
            matrix[p][q] += 1

for p in range(1, n[0] + 1):
    for q in range(1, n[1] + 1):
        if matrix[p + 1][q + 1] == "*" and matrix[p][q] != "*":
            matrix[p][q] += 1

for i in range(1, n[0] + 1):
    for j in range(1,  n[1] + 1):
        print(matrix[i][j], end =' ')
    print()

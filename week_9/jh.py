import copy
X = [[1, 1, 1],
     [0, 2, 0],
     [0, 0, 4]]

c = [1, 1, 1]

indexes = list(range(len(X)))
for diag_elem in range(len(X)):
    diag_scaled = 1.0 / X[diag_elem][diag_elem]
    for j in range(len(X)):
        X[diag_elem][j] *= diag_scaled
    c[diag_elem] *= diag_scaled
    for k in indexes[0:diag_elem] + indexes[diag_elem + 1:]:
        crScaled = X[k][diag_elem]
        for j in range(len(X)):
            X[k][j] = X[k][j] - crScaled * X[diag_elem][j]
        c[k] = c[k] - crScaled * c[diag_elem]
print(X)
print(c)



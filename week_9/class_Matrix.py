from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def size(self):
        sp = (len(self.matrix), len(self.matrix[0]))
        return sp

    def __add__(self, other):
        if self.size() == other.size():
            list_of_lists = []
            for i in range(self.size()[0]):
                newList = []
                for j in range(self.size()[1]):
                    newList.append(self.matrix[i][j] + other.matrix[i][j])
                list_of_lists.append(newList)
            return Matrix(list_of_lists)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            newlist = []
            for i in range(self.size()[0]):
                newList = []
                for j in range(self.size()[1]):
                    newList.append(self.matrix[i][j] * other)
                newlist.append(newList)
            return Matrix(newlist)
        elif isinstance(other, Matrix) \
                and self.size()[1] == other.size()[0]:
            newlist = [[0 for row in range(other.size()[1])]
                       for col in range(self.size()[0])]
            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    for p in range(other.size()[0]):
                        newlist[i][j] += self.matrix[i][p] * other.matrix[p][j]
            return Matrix(newlist)
        else:
            raise MatrixError(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def transpose(self):
        self.matrix = list(zip(*self.matrix))
        return Matrix(self.matrix)

    def transposed(self):
        return Matrix(list(zip(*self.matrix)))

    def solve(self, other):
        if self.size()[0] == self.size()[1]:
            X = self.matrix
            c = other
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
            return c
        else:
            raise MatrixError(self, other)


class SquareMatrix(Matrix):

    def __pow__(self, power):
        if self.size()[0] == self.size()[1]:
            if power == 0:
                I = [[0 for _ in range(self.size()[1])]
                     for _ in range(self.size()[0])]
                for i in range(self.size()[0]):
                    for j in range(self.size()[1]):
                        if i == j:
                            I[i][j] = 1
                        else:
                            I[i][j] = 0
                return Matrix(I)
            elif power == 1:
                return self.__str__()
            elif power > 1:
                if power % 2 == 0:
                    power = power / 2
                    return self.__pow__(self, power / 2)
                else:
                    return self * self.__pow__(self)



m = SquareMatrix([[1, 1, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 0, 1]]
                 )
# print(m)
print('----------')
# print(m ** 1)
print('----------')
#print(m ** 2)
print('----------')
print(m ** 3)
print('----------')
# print(m ** 4)
print('----------')
# print(m ** 5)
jhbjh
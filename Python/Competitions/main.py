from copy import deepcopy


def f(l1, l2):
    res = 0
    for i in range(len(l1)):
        res += (l1[i] * l2[i])
    return res


def cols(m, index):
    res = []
    for i in range(len(m)):
        res.append(m[i][index])
    return res


class Matrix:
    def __init__(self, L):
        self.L = L

    def __str__(self):
        s = ''
        for i in range(len(self.L)):
            for j in range(len(self.L[0])):
                s += (str(self.L[i][j]) + ' ')
            s += '\n'
        return s

    def __getitem__(self, index):
        return self.L[index]

    def __delitem__(self, key):
        return self.L[key]

    def __len__(self):
        return len(self.L)

    def __add__(self, other):
        for i in range(len(other.L)):
            for j in range(len(other.L[0])):
                other.L[i][j] += self[i][j]
        return other

    def __radd__(self, other):
        return other + self

    def __mul__(self, other):
        if isinstance(other, Matrix):
            res = Matrix([[0 for j in range(len(self.L))] for i in range(len(other[0]))])
            for i in range(len(res.L)):
                for j in range(len(res.L[0])):
                    res[i][j] = f(self[i], cols(other.L, j))
        else:
            res = Matrix(deepcopy(self.L))
            for i in range(len(self.L)):
                for j in range(len(self[0])):
                    res[i][j] *= other
        return res

    def __rmul__(self, other):
        return other * self

    def minor(self, j):
        M = self.L[1:]
        for i in range(len(M)):
            M[i].pop(j)
        res = Matrix(M)
        return res

    def det(self):
        if len(self) != len(self[0]):
            return None
        elif len(self) == 1:
            return self[0][0]
        elif len(self) == 2:
            return self[0][0] * self[1][1] - self[1][0] * self[0][1]
        else:
            determinant = 0
            signum = 1
        for j in range(len(self)):
            determinant += self[0][j] * signum * self.minor(j).det()
            signum *= -1
        return determinant;


A = Matrix([[10, -4, 3],
            [11, -4, 5],
            [3, -1, 4]])
print(A.det())

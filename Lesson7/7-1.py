# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return '\n'.join('\t'.join(f'{itm:02}' for itm in line) for line in self.matrix)
#
#     def __add__(self, other):
#         try:
#             c = []
#             for i in range(len(self.matrix)):
#                 c.append([])
#                 for j in range(len(self.matrix[0])):
#                     c[i].append(self.matrix[i][j] + other.matrix[i][j])
#             return '\n'.join('\t'.join(f'{itm:02}' for itm in line) for line in c)
#         except IndexError:
#             return f'Матрицы разных размерностей!'
#
#
# matrix_1 = Matrix([[10, 23], [17, 55], [111, 213]])
# matrix_2 = Matrix([[12, 24], [13, 52], [11, 21]])
#
# print(matrix_1 + matrix_2)

import numpy as np

m_1 = np.array([[10, 23], [17, 55], [111, 123]])
m_2 = np.array([[12, 24], [13, 52], [11, 21]])


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(f'{itm:02}' for itm in line) for line in self.matrix)

    def __add__(self, other):
        try:
            c = self.matrix + other.matrix
            return Matrix(c)
        except ValueError:
            return f'Матрицы разных размерностей!'


matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)

print(matrix_1 + matrix_2)

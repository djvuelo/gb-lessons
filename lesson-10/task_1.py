class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda line: ' '.join(map(str, line)), self.matrix))

    def __add__(self, other):
        new_matrix = []
        for i in range(0, len(self.matrix)):
            new_matrix.append([])
            for j in range(0, len(self.matrix[0])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5], [2, 4], [-1, 64]])
print(matrix1)
print('+')
print(matrix2)
print('=')
print(f'{matrix1 + matrix2}')

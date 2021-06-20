class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda line: ' '.join(map(str, line)), self.matrix)) + '\n' + '-' * 10


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matrix1)
print(matrix2)
print(matrix3)

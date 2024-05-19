def matrix_multiplication(matrix1, matrix2, n, m):
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = 0
            for k in range(m):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return matrix
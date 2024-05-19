def sum_matrix(matrix1, matrix2, n, m):
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix





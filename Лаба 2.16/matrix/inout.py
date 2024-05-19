from random import uniform


def input_matrix(A, n, m, a, b):
    for i in range(n):
        for j in range(m):
            A[i][j] = uniform(a, b)
    return A


def matrix_output(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(round(matrix[i][j], 3), end="\t")
        print()
    print()

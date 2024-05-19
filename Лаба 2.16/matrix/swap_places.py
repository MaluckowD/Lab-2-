def swap_rows(matrix, k, l):
    matrix[k - 1], matrix[l - 1] = matrix[l - 1], matrix[k - 1]
    return matrix

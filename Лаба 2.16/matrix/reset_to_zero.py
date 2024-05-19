def zero_row_col(matrix):
    min_val = 100000
    min_row = 0
    min_col = 0

    # Находим минимальный элемент матрицы и его индексы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_row = i
                min_col = j

    # Обнуляем строку
    for j in range(len(matrix[0])):
        matrix[min_row][j] = 0

    # Обнуляем столбец
    for i in range(len(matrix)):
        matrix[i][min_col] = 0

    return matrix

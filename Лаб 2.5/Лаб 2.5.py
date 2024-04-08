from random import uniform
import numpy as np
def input_matrix(matrix):
    a = int(input("Введите левый конец диапазона:"))
    b = int(input("Введите правый конец диапазона:"))
    # ввод элементов матрицы через генератор случайных чисел;
    for i in range(n):
        for j in range(n):
            matrix[i][j] = uniform(a, b)

def matrix_output(matrix):
    for i in range(n):
        for j in range(n):
            print(round(matrix[i][j],3), end="\t")
        print()
    print()
n = int(input("Введите размерность матриц A и B:"))
if n > 0:
    A = [[0] * n for i in range(n)]
    B = [[0] * n for j in range(n)]
    input_matrix(A)
    input_matrix(B)
    print("Вы ввели следующую матрицу A:")
    matrix_output(A)
    print("Вы ввели следующую матрицу B:")
    matrix_output(B)
    Z = np.transpose(A) + B
    Z = np.round(Z,3)
    print("Матрица Z равна:")
    matrix_output(Z)
    print()
    Y = np.transpose(B) + A
    Y = np.round(Y,3)
    print("Матрица Y равна:")
    matrix_output(Y)
else:
    print("Вы ввели неккорекную длину массивов A и B")
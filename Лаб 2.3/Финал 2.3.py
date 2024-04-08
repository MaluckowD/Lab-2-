import numpy as np
from random import uniform
from time import perf_counter_ns
def matrix_output(matrix):
    for i in range(n):
        for j in range(n):
            print(round(matrix[i][j],3), end="\t")
        print()
    print()

def min_mean(matrix):
    min_line_mean = 10 * 10
    for line in matrix:
        line_sum = 0
        for num in line:
           line_sum += num
        line_avg = line_sum / n
        if line_avg < min_line_mean:
            min_line_mean = line_avg
    print(round(min_line_mean,3))

def matrix_multiplication(matrix1,matrix2):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 0
            for k in range(n):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    matrix_output(matrix)
    return matrix

def sum_matrix(matrix1,matrix2):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    matrix_output(matrix)
    return matrix

def matrix_difference(matrix1,matrix2):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix1[i][j] - matrix2[i][j]
    matrix_output(matrix)
    return matrix

n = 5
A = [[0] * n for i in range(n)]
quary = str(input("Введите способ задания массива:"))
if quary == 'клавиатура':
    #ввод элементов матрицы с клавиатуры;
    for i in range(n):
        for j in range(n):
            print("A[", i, "][",j,"]=", end="")
            A[i][j] = float(input())
    print("Вы ввели следующую матрицу A через клавиатуру:")
    matrix_output(A)
elif quary == "random":
    a = int(input("Введите левый конец диапазона:"))
    b = int(input("Введите правый конец диапазона:"))
    # ввод элементов матрицы через генератор случайных чисел;
    for i in range(n):
        for j in range(n):
            A[i][j] = uniform(a, b)
    print("Вы ввели следующую матрицу через модуль random:")
    matrix_output(A)
else:
    print("Вы ввели неккоректный способ ввода")
    exit()

t_start = perf_counter_ns()
print("Решение без методов списка:")
print("Наименьшее значение среди средних из строк матрицы A:")
min_mean(A)
print("Произведение матриц A*A=A2:")
A2 = matrix_multiplication(A,A)
print("Произведение матриц A2*A=A3:")
A3 = matrix_multiplication(A2,A)
print("Произведение матриц A3*A=A4:")
A4 = matrix_multiplication(A3,A)
print("Произведение матриц A4*A=A5:")
A5 = matrix_multiplication(A4,A)
print("Сумма матриц A2+A3=B1:")
B1 = sum_matrix(A2,A3)
print("Сумма матриц A4+A5=B2:")
B2 = sum_matrix(A4,A5)
print("Разность матриц B1-B2=B:")
B = matrix_difference(B1,B2)
print("Наименьшее значение среди средних из строк матрицы B:")
min_mean(B)
#транспонирование матрицы;
Bt = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        Bt[i][j] = B[j][i]
print("Транспонированная матрица B:")
matrix_output(Bt)
print("Произведение матриц A*Bt=C1:")
C1 = matrix_multiplication(A,Bt)
print("Произведение матриц Bt*A=C2:")
C2 = matrix_multiplication(Bt,A)
print("Разность матриц C1-C2=C:")
C = matrix_difference(C1,C2)
print("Наименьшее значение среди средних из строк матрицы C:")
min_mean(C)
all_time = perf_counter_ns() - t_start
print("Время работы без использования встроенных методов", all_time,"ms")

t_start = perf_counter_ns()
print("Решение с применением numpy:")
line_means = np.mean(A, axis=1)
min_meanA = np.min(line_means)
print("Наименьшее значение среди средних из строк матрицы A:")
print(round(min_meanA,3))
A2 = np.matmul(A, A)
A2 = np.around(A2,3)
print("Произведение матриц A*A=A2:")
print(A2)
print()
A3 = np.matmul(A2, A)
A3 = np.round(A3,3)
print("Произведение матриц A2*A=A3:")
print(A3)
print()
A4 = np.matmul(A3, A)
A4 = np.round(A4,3)
print("Произведение матриц A3*A=A4:")
print(A4)
print()
A5 = np.matmul(A4, A)
A5 = np.round(A5,3)
print("Произведение матриц A4*A=A5:")
print(A5)
print()
B = A2 + A3 - A4 - A5
print("Матрица B равна:")
print(B)
print()
line_means = np.mean(B, axis=1)
min_meanB = np.min(line_means)
print("Наименьшее значение среди средних из строк матрицы B:")
print(round(min_meanB,3))
BT = np.transpose(B)
print("Транспонированная матрица B:")
print(BT)
print()
C1 = np.matmul(A, BT)
C1 = np.round(C1,3)
print("Произведение матриц A*Bt=C1:")
print(C1)
print()
C2 = np.matmul(BT, A)
C2 = np.round(C2,3)
print("Произведение матриц Bt*A=C2:")
print(C2)
print()
C = C1 - C2
print("Разность матриц C1-C2=C:")
print(C)
print()
line_means = np.mean(C, axis=1)
min_meanC = np.min(line_means)
print("Наименьшее значение среди средних из строк матрицы C:")
print(round(min_meanC,3))
all_time = perf_counter_ns() - t_start
print("Время работы c использованием numpy", all_time,"ms")




from random import uniform

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

n = int(input("Введите размер матрицы A:"))
if n > 0:
    A = [[0] * n for i in range(n)]
else:
    print("Вы ввели неправильный размер матрицы")
    exit()
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

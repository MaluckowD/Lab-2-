import numpy as np
n = 5
A = [[0] * n for i in range(n)]
#ввод элементов матрицы с клавиатуры;
for i in range(n):
    for j in range(n):
        print("A[", i, "][",j,"]=", end="")
        A[i][j] = float(input())
print("Вы ввели следующую матрицу A через клавиатуру:")
for i in range(n):
    for j in range(n):
        print(A[i][j], end="\t")
    print()
print()
line_means = np.mean(A, axis=1)
min_meanA = np.min(line_means)
print(min_meanA)
A2 = np.matmul(A, A)
print(A2)
print()
A3 = np.matmul(A2, A)
print(A2)
print()
A4 = np.matmul(A3, A)
print(A4)
print()
A5 = np.matmul(A4, A)
print(A5)
print()
B = A2 + A3 - A4 - A5
print(B)
print()
line_means = np.mean(B, axis=1)
min_meanB = np.min(line_means)
print(min_meanB)
BT = np.transpose(B)
print(BT)
print()
C1 = np.matmul(A, BT)
print(C1)
print()
C2 = np.matmul(BT, A)
print(C2)
print()
C = C1 - C2
print(C)
print()
line_means = np.mean(C, axis=1)
min_meanC = np.min(line_means)
print(min_meanC)


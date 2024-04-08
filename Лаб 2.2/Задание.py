from random import uniform


def get_average_line(matrix, line):
    summ_1 = k_1 = 0
    summ_2 = k_2 = 0
    for i in range(len(matrix[line])):
        if i % 2 == 0:
            summ_1 += matrix[line][i]
            k_1 += 1
        else:
            summ_2 += matrix[line][i]
            k_2 += 1

    average_1 = summ_1 / k_1
    average_2 = summ_2 / k_2

    return [average_1, average_2]


n = int(input("Введите количество столбцов матрицы:"))
m = int(input("Введите количество строк матрицы:"))
a = [[0] * m for k in range(n)]
x = int(input("Введите левый конец диапазона:"))
y = int(input("Введите правый конец диапазона:"))
for i in range(n):
    for j in range(m):
        a[i][j] = round(uniform(x, y))

print(*a, sep="\n")
print()

b = [[0 for _ in range(m)] for _ in range(n)]
c = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    averages = get_average_line(a, i)
    for j in range(m):
        if (i + j) % 2 == 0:
            c[i][j] = a[i][j]
            b[i][j] = averages[0]
        else:
            # print(i, j)
            b[i][j] = a[i][j]
            c[i][j] = averages[1]

print(*b, sep="\n")
print()
print(*c, sep="\n")


import copy
from random import uniform
from time import perf_counter_ns
n = 5
m = 4
def without_methods(matrix):
    t_start = perf_counter_ns()
    # минимальный элемент и определение его индексов без использования встроенных методов;
    min_element = matrix[0][0]
    min_row = 0
    min_column = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_row = i
                min_column = j

    print("Минимальный элемент матрицы без использования встроенных методов =", round(min_element,4))
    print("Элемент расположен в", min_row + 1, "строке и в", min_column + 1, "столбце")

    # обнуление элементов матрицы без использования встроенных методов;
    for i in range(min_row + 1, n):
        for j in range(min_column + 1, m):
            matrix[i][j] = 0

    # вывод измененной матрицы;
    print("Получена следующая матрица без использования встроенных методов:")
    for i in range(n):
        for j in range(m):
            print(round(matrix[i][j],4), end="\t")
        print()
    all_time = perf_counter_ns() - t_start
    print("Время работы без использования встроенных методов",all_time,"ms")


def with_methods(matrix):
    t_start = perf_counter_ns()
    # минимальный элемент матрицы через встроенные методы и определение его индексов;
    minimum = min([min(l) for l in matrix])
    index_i = index_j = 0
    for i in range(n):
        try:
            #index_i = matrix[i].index(minimum)
            #index_j = i
            index_j = matrix[i].index(minimum)
            index_i = i
            break
        except:
            ...

    print("Минимальный элемент матрицы через использование встроенных методов =", round(minimum,4))
    print("Элемент расположен в", index_i + 1, "строке и в", index_j + 1, "столбце")

    # обнуление элементов матрицы с использованием встроенных методов;
    for i in range(index_i + 1, n):
        for j in range(index_j + 1, m):
            matrix[i].pop(j)
            matrix[i].insert(j, 0)

    # вывод измененной матрицы;
    print("Получена следующая матрица с использованием встроенных методов:")
    for i in range(n):
        for j in range(m):
            print(round(matrix[i][j],4), end="\t")
        print()
    all_time = perf_counter_ns() - t_start
    print("Время работы с использованием встроенных методов",all_time,"ms")

quary = str(input("Введите способ задания массива:")).lower().strip()
if quary == 'клавиатура':
    n = int(input("Введите количество столбцов матрицы:"))
    m = int(input("Введите количество строк матрицы:"))
    if n > 0 and m >0:
        matrix1 = [[0] * m for i in range(n)]
        # ввод элементов матрицы с клавиатуры;
        for i in range(n):
            for j in range(m):
                print("matrix1[", i, "][", j, "]=", end="")
                matrix1[i][j] = float(input())

        print("Вы ввели следующую матрицу через клавиатуру:")
        for i in range(n):
            for j in range(m):
                print(matrix1[i][j], end="\t")
            print()
        matrix3 = copy.deepcopy(matrix1)
        without_methods(matrix1)
        with_methods(matrix3)
    else:
        print("Вы ввели некорректные данные")
elif quary == "random":
    n = int(input("Введите количество столбцов матрицы:"))
    m = int(input("Введите количество строк матрицы:"))
    if n > 0 and m > 0:
        a = int(input("Введите левый конец диапазона:"))
        b = int(input("Введите правый конец диапазона:"))
        matrix2 = [[0] * m for k in range(n)]
        # ввод элементов матрицы через генератор случайных чисел;
        for i in range(n):
            for j in range(m):
                matrix2[i][j] = uniform(a, b)

        print("Вы ввели следующую матрицу через модуль random:")
        for i in range(n):
            for j in range(m):
                print(round(matrix2[i][j], 4), end="\t")
            print()
        matrix4 = copy.deepcopy(matrix2)
        without_methods(matrix2)
        with_methods(matrix4)
    else:
        print("Вы ввели некорректные данные")
else:
    print("Вы ввели неккоректный способ ввода")
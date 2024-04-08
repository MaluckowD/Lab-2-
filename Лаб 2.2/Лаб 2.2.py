import copy
n = 5
m = 4
matrix = [[0] * m for i in range(n)]

#ввод элементов матрицы с клавиатуры;
for i in range(n):
    for j in range(m):
        print("A[", i, "][",j,"]=", end="")
        matrix[i][j] = int(input())

#вывод матрицы;
print("Вы ввели следующую матрицу:")
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end="\t")
    print()

matrix1 = copy.deepcopy(matrix)

#минимальный элемент и определение его индексов без использования встроенных методов;
min_element = matrix[0][0]
min_row = 0
min_column = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
            min_row = i
            min_column = j

print("Минимальный элемент матрицы без использования встроенных методов =",min_element)
print("Элемент расположен в",min_row + 1,"строке и в",min_column + 1,"столбце")

# обнуление элементов матрицы без использования встроенных методов;
for i in range(min_row + 1, n):
    for j in range(min_column + 1, m):
        matrix[i][j] = 0

# вывод измененной матрицы;
print("Получена следующая матрица без использования встроенных методов:")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="\t")
    print()

#минимальный элемент матрицы через встроенные методы и определение его индексов;
a1 = min([min(l) for l in matrix1])
inp = index = 0
for i in range(n):
    try:
        inp = matrix1[i].index(a1)
        index = i
        break
    except:
        ...

print("Минимальный элемент матрицы через использование встроенных методов =",a1)
print("Элемент расположен в",index + 1,"строке и в",inp + 1,"столбце")


#обнуление элементов матрицы с использованием встроенных методов;
for i in range(index + 1, n):
    for j in range(inp + 1, m):
        matrix1[i].pop(j)
        matrix1[i].insert(j, 0)

#вывод измененной матрицы;
print("Получена следующая матрица с использованием встроенных методов:")
for i in range(n):
    for j in range(m):
        print(matrix1[i][j],end="\t")
    print()




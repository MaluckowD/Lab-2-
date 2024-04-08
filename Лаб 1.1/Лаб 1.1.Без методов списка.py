n = 5
m = 4
matrix = [[0] * m for i in range(n)]


#ввод элементов матрицы;
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())

#вывод матрицы;
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end="\t")
    print()
inp = index = 0
a1 = min([min(l) for l in matrix])

for i in range(n):
    try:
        inp = matrix[i].index(a1)
        index = i
        print(index,inp)
        break
    except:
        ...
for i in range(index + 1, n):
    for j in range(inp + 1, m):
        matrix[i].pop(j)
        matrix[i].insert(j, 0)
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end="\t")
    print()


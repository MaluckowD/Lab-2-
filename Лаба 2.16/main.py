import matrix.inout as io
import matrix.swap_places as sw
import matrix.reset_to_zero as rz
import matrix.multiplication as mp
import matrix.sum as sm


def main():
    while True:
        print("\nМеню:")
        print("1. Поменять местами k-ю и l-ю строки в матрице;")
        print(
            "2. Обнулить все элементы строки и столбца, на пересечении которых расположен минимальный элемент матрицы;")
        print("3. Перемножить две матрицы; ")
        print("4. Сложить две матрицы.")

        choice = input("Выберите действие: ")

        if choice == '1':
            m = int(input("Введите количество столбцов матрицы: "))
            n = int(input("Введите количество строк матрицы: "))
            a = int(input("Введите левый конец диапазона: "))
            b = int(input("Введите правый конец диапазона: "))
            A = [[0] * m for i in range(n)]
            matrix = io.input_matrix(A, n, m, a, b)
            print("Исходная матрица:\n")
            io.matrix_output(matrix, n, m)
            k = int(input("Введите первую строку,которую хотите поменять местами: "))
            l = int(input("Введите вторую строку,которую хотите поменять местами: "))
            if k > n or l > n:
                print("Вы вышли за пределы матрицы")
                break
            matrix = sw.swap_rows(matrix, k, l)
            print("Преобразованная матрица:\n")
            io.matrix_output(matrix, n, m)
        elif choice == '2':
            m = int(input("Введите количество столбцов матрицы: "))
            n = int(input("Введите количество строк матрицы: "))
            a = int(input("Введите левый конец диапазона: "))
            b = int(input("Введите правый конец диапазона: "))
            A = [[0] * m for i in range(n)]
            matrix = io.input_matrix(A, n, m, a, b)
            print("Исходная матрица:\n")
            io.matrix_output(matrix, n, m)
            matrix = rz.zero_row_col(matrix)
            print("Преобразованная матрица:\n")
            io.matrix_output(matrix, n, m)
        elif choice == '3':
            m = int(input("Введите количество столбцов матрицы 1 и количество строк матрицы 2: "))
            n = int(input("Введите количество строк матрицы 1: "))
            a = int(input("Введите левый конец диапазона: "))
            b = int(input("Введите правый конец диапазона: "))
            A = [[0] * m for i in range(n)]
            matrix1 = io.input_matrix(A, n, m, a, b)
            print("Исходная матрица 1:\n")
            io.matrix_output(matrix1, n, m)

            k = int(input("Введите количество столбцов матрицы 2: "))
            a1 = int(input("Введите левый конец диапазона: "))
            b1 = int(input("Введите правый конец диапазона: "))
            B = [[0] * k for i in range(m)]
            matrix2 = io.input_matrix(B, m, k, a1, b1)
            print("Исходная матрица 2:\n")
            io.matrix_output(matrix2, m, k)

            result = mp.matrix_multiplication(matrix1, matrix2, n, k)

            print("Итоговая матрица:\n")
            io.matrix_output(result, n, k)
        elif choice == '4':
            m = int(input("Введите количество столбцов матрицы 1 и количество столбцов матрицы 2: "))
            n = int(input("Введите количество строк матрицы 1 и количество строк матрицы 2: "))
            a = int(input("Введите левый конец диапазона: "))
            b = int(input("Введите правый конец диапазона: "))
            A = [[0] * m for i in range(n)]
            matrix1 = io.input_matrix(A, n, m, a, b)
            print("Исходная матрица 1:\n")
            io.matrix_output(matrix1, n, m)
            B = [[0] * m for i in range(n)]
            matrix2 = io.input_matrix(B, n, m, a, b)
            print("Исходная матрица 2:\n")
            io.matrix_output(matrix2, n, m)
            result = sm.sum_matrix(matrix1, matrix2, n, m)
            print("Итоговая матрица:\n")
            io.matrix_output(result, n, m)
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

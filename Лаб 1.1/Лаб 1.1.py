"""
Лабораторная работа 1
Тема: Обработка одномерных массивов.
Цель: Научиться работать с одномерными массивами.
Переменные:
  N - количество элементов исходного массива;
  элементы массива
Программист: Малюков Дмитрий Иванович
Дата написания: 05.02.2024
"""

# С использованием встроенных методов;
import copy
from random import uniform
from time import perf_counter_ns

def without_methods(A):
    t_start = perf_counter_ns()
    # Без использования встроенных методов;
    s = 0
    for i in range(N):
        s += A[i]
    sr1 = s / N
    s1 = 0
    k = 0
    for i in range(N):
        if A[i] > sr1:
            k += 1
            s1 += A[i]
    ans1 = s1 / k
    print("Исходный массив  равен", A, "среднее арифметическое его элементов = ", round(sr1,3))
    print("Результат без использования методов", round(ans1, 3))

    all_time = perf_counter_ns() - t_start
    print("Время работы без использования встроенных методов", all_time)


def with_methods(A):
    t_start = perf_counter_ns()
    # С использованием встроенных методов;
    B = []
    sr2 = sum(A)/len(A)

    for i in range(N):
        if A[i] > sr2:
            B.append(A[i])
    ans2 = sum(B) / len(B)
    print("Исходный массив  равен",A,"среднее арифметическое его элементов = ",round(sr2,3))
    print("Новый массив B =",B)
    print("Результат (с использованием встроенных методов) =",round(ans2,3))

    all_time = perf_counter_ns() - t_start
    print("Время работы с использованием встроенных методов",all_time)

quary = str(input("Введите способ задания массива:"))
if quary == 'клавиатура':
    N = int(input("Введите количество элементов исходного массива:"))
    if N > 0:
        A1 = [0] * N
        #ввод элементов массива с клавиатуры;
        for i in range(N):
            print("A[", i, "]=", end="")
            A1[i] = float(input())
        print("Вы ввели следующий массив через клавиатуру:")
        print(A1)
        A3 = copy.deepcopy(A1)
        without_methods(A1)
        with_methods(A3)
    else:
        print("Вы ввели неккоректную длину массива")

elif quary == "random":
    N = int(input("Введите количество элементов исходного массива:"))
    if N > 0:

        #ввод элементов массива через random;
        a = int(input("Введите левый конец диапазона"))
        b = int(input("Введите правый конец диапазона"))
        A2 = [0] * N
        for i in range(N):
            A2[i] = uniform(a,b)
        A2 = [round(i,4) for i in A2]

        print("Вы ввели следующий массив через модуль random:")
        print(A2)
        A4 = copy.deepcopy(A2)

        without_methods(A2)
        with_methods(A4)
    else:
        print("Вы ввели неккоректную длину массива")


else:
    print("Вы ввели неккоректный способ ввода")









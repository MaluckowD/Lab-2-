database = {'1': ['Шарапов', 'Василий', 'Иванович', '5', 'варщик', '50000'],
            '2': ['Иванов', 'Иван', 'Иванович', '3', 'станочник', '50000'],
            '3': ['Шарапов', 'Василий', 'Иванович', '3', 'варщик', '10000'],
            '4': ['Егоров', 'Василий', 'Иванович', '5', 'станочник', '500']
            }


def view_all_records():
    print('Запись'.center(15), 'Фамилия'.center(15), 'Имя'.center(12),
          'Отчество'.center(17), 'Цех'.center(17), 'Должность'.center(17),
          'Оклад'.center(15))
    print(''.center(15, '-'), ''.center(15, '-'), ''.center(12, '-'),
          ''.center(17, '-'), ''.center(17, '-'), ''.center(17, '-'), ''.center(15, '-'))
    for key, val in database.items():
        print(key.center(15), val[0].center(15), val[1].center(12),
              val[2].center(17), val[3].center(17), val[4].center(17),
              val[5].center(15))


def add_records(n):
    for i in range(n):
        key = input("Введите номер сотрудника:")
        fam = input("Введите фамилию: ")
        name = input("Введите имя: ")
        otchestvo = input("Введите отчество: ")
        workshop = input("Введите номер цеха: ")
        post = input("Введите занимаемую должность: ")
        salary = input("Введите оклад: ")
        database[key] = [fam, name, otchestvo, workshop, post, salary]


def delete_record_by_key(key):
    if key in database:
        del database[key]
        print(f"Запись с ключом {key} удалена.")
    else:
        print("Запись с таким ключом не найдена.")


def calculate_average(department):
    total_salary = 0
    count = 0
    for key, val in database.items():
        if int(val[3]) == department:
            total_salary += int(val[5])
            count += 1
    if count == 0:
        print("Нет сотрудников в данном цехе.")
    else:
        avg_salary = total_salary / count
        print(f"Средняя заработная плата в цехе {department}: {avg_salary}")


def calculate_average_by_post(post):
    total_salary = 0
    count = 0
    for key, val in database.items():
        if val[4] == post:
            total_salary += int(val[5])
            count += 1
    if count == 0:
        print("Нет сотрудников с данной должностью.")
    else:
        avg_salary = total_salary / count
        print(f"Средняя заработная плата для должности {post}: {avg_salary}")


def main_menu():
    while True:
        print("\nМеню:")
        print("1. Просмотр всех записей в базе данных")
        print("2. Добавление N записей")
        print("3. Удаление записи по ключу")
        print("4. Поиск необходимой информации")
        print("5. Завершение работы с базой данных")

        choice = input("Выберите действие: ")

        if choice == '1':
            view_all_records()
        elif choice == '2':
            n = int(input("Введите количество записей для добавления: "))
            add_records(n)
        elif choice == '3':
            key = input("Введите ключ записи для удаления: ")
            delete_record_by_key(key)
        elif choice == '4':
            search_criteria = input("Введите номер цеха или должность: ")
            if search_criteria.isdigit():
                calculate_average(int(search_criteria))
            else:
                calculate_average_by_post(search_criteria)
        elif choice == '5':
            print("Работа с базой данных завершена.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()

# ctrl + alt + l

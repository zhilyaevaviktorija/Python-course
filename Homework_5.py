# Условия в Python

"""
Блок 1: задачи на условия

Задание 1. Напишите программу для проверки пароля пользователя

Образец работы программы:
    Введите пароль: 123
    Пароль неверный
    Введите пароль: 321
    Пароль верный

Алгоритм:
    Создайте переменную, в которой хранится верный пароль
    Запросите у пользователя пароль
    Если пароль верный, выведите "Пароль верный"
    Иначе, выведите "Пароль неверный"
"""

# password = "321"
# user_password = input("Введите пароль: ")
# if user_password == password:
#     print("Пароль верный")
# else:
#     print("Пароль неверный")


"""
Задание 2. Напишите программу для проверки возраста пользователя с использованием тернарного оператора

Образец работы программы:
    Введите возраст: 12
    Доступ запрещен
    Введите возраст: 21
    Доступ разрешен

Задача: Напишите код с использованием тернарного оператора
"""

# age = int(input("Введите возраст: "))
# has_access = "Доступ разрешен" if age >= 18 else "Доступ запрещен"
# print(has_access)


"""
Задание 3. Напишите программу для приветствия пользователя с вложенными условиями

Образец работы программы:
    Введите время: 12:30
    Добрый день!
    Введите время: 10:30
    Доброе утро!
    Введите время: 21:30
    Добрый вечер!
    Введите время: 01:30
    Доброй ночи!

Задача: Используйте вложенные условия вместо цепочки elif
"""

# time = input("Введите время: ")
# hours = int(time.split(':')[0])  # Извлекаем часы
#
# if hours >= 0:
#     if hours >= 18:
#         print("Добрый вечер!")
#     else:
#         if hours >= 12:
#             print("Добрый день!")
#         else:
#             if hours >= 6:
#                 print("Доброе утро!")
#             else:
#                 print("Доброй ночи!")


"""
Задание 4. Умный калькулятор с проверкой типов

Образец работы программы:
    Введите выражение: 2 + 2
    4
    Введите выражение: 2 == 2
    True
    Введите выражение: 2 + 2.1
    4.1
    Введите выражение: abc + 2
    Ошибка: неверный формат чисел

Задача: Добавьте проверку типов с помощью isinstance
"""

# expression = input("Введите выражение: ").strip()
#
# try:
#     result = None
#
#     # Обрабатываем пробелы вокруг операторов
#     if '+' in expression:
#         parts = [part.strip() for part in expression.split('+')]
#         if len(parts) == 2:
#             num1 = float(parts[0]) if '.' in parts[0] else int(parts[0])
#             num2 = float(parts[1]) if '.' in parts[1] else int(parts[1])
#             result = num1 + num2
#
#     elif '-' in expression:
#         parts = [part.strip() for part in expression.split('-')]
#         if len(parts) == 2:
#             num1 = float(parts[0]) if '.' in parts[0] else int(parts[0])
#             num2 = float(parts[1]) if '.' in parts[1] else int(parts[1])
#             result = num1 - num2
#
#     elif '*' in expression:
#         parts = [part.strip() for part in expression.split('*')]
#         if len(parts) == 2:
#             num1 = float(parts[0]) if '.' in parts[0] else int(parts[0])
#             num2 = float(parts[1]) if '.' in parts[1] else int(parts[1])
#             result = num1 * num2
#
#     elif '/' in expression:
#         parts = [part.strip() for part in expression.split('/')]
#         if len(parts) == 2:
#             num1 = float(parts[0]) if '.' in parts[0] else int(parts[0])
#             num2 = float(parts[1]) if '.' in parts[1] else int(parts[1])
#             result = num1 / num2
#
#     elif '==' in expression:
#         parts = [part.strip() for part in expression.split('==')]
#         if len(parts) == 2:
#             try:
#                 num1 = float(parts[0]) if '.' in parts[0] else int(parts[0])
#                 num2 = float(parts[1]) if '.' in parts[1] else int(parts[1])
#                 result = num1 == num2
#             except ValueError:
#                 result = parts[0] == parts[1]
#     else:
#         raise ValueError("Неподдерживаемая операция")
#
#     # Проверяем, что result был вычислен
#     if result is None:
#         raise ValueError("Не удалось вычислить выражение")
#
#     # Проверка типов с помощью isinstance
#     is_number = isinstance(result, (int, float)) and not isinstance(result, bool)
#     is_boolean = isinstance(result, bool)
#
#     if is_number:
#         if isinstance(result, float) and result.is_integer():
#             print(int(result))
#         else:
#             print(result)
#     elif is_boolean:
#         print(result)
#     else:
#         print(f"Результат: {result}")
#
# except ValueError as e:
#     print(f"Ошибка: {e}")
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль")
# except Exception as e:
#     print(f"Неизвестная ошибка: {e}")


"""
Задание 5. Проверка сложного пароля с any()

Образец работы программы:
    Введите пароль: abc
    Пароль слишком простой
    Введите пароль: abc123
    Пароль принят!

Условия: Пароль должен содержать хотя бы одну цифру

Задача: Используйте any() для проверки наличия цифр в пароле
"""

# password = input("Введите пароль: ")
# has_digit = any(char.isdigit() for char in password)
# if has_digit:
#     print("Пароль принят!")
# else:
#     print("Пароль слишком простой")


"""
Блок 2: задачи на обработку данных

Задание 6. Фильтрация данных с any()

Образец результата работы программы:
    Laptop
    Smartphone
    Tablet

Условия:
Дан список продуктов в магазине техники:
    ["Laptop True", "Headphones False", "Smartphone True", "Tablet True", "Speaker False"]

Задача: Используйте any() для проверки, есть ли в магазине хотя бы один продукт в наличии
"""

# Список продуктов
# products = ["Laptop True", "Headphones False", "Smartphone True", "Tablet True", "Speaker False"]
#
# # Проверяем, есть ли хотя бы один продукт в наличии с помощью any()
# has_available_products = any("True" in product for product in products)
#
# if has_available_products:
#     print("В магазине есть товары в наличии!")
#     # Выводим продукты в наличии
#     for product in products:
#         if "True" in product:
#             product_name = product.split()[0]  # Извлекаем название продукта
#             print(product_name)
# else:
#     print("Все товары распроданы!")


"""
Задание 7. Фильтрация по сложному условию

Образец результата работы программы:
    Товары с количеством от 10 до 40:
    Headphones 12
    Tablet 10

Условия:
Дан список продуктов:
    ["Laptop 8", "Headphones 12", "Smartphone 41", "Tablet 10", "Speaker 6"]

Задача: Найдите товары с количеством от 10 до 40 включительно
"""

# num_products = ["Laptop 8", "Headphones 12", "Smartphone 41", "Tablet 10", "Speaker 6"]
#
# print("Товары с количеством от 10 до 40: ")
# # Для каждого продукта
# for product in num_products:
#     # Создаем переменные name и quantity с помощью split()
#     name, quantity_str = product.split()
#     quantity = int(quantity_str)
#
#     # Проверяем количество (от 10 до 40)
#     if 10 <= quantity <= 40:
#         # Выводим на экран название продукта и его количество
#         print(f"{name} {quantity}")


"""
Задание 8. Обработка данных с проверкой типов

Образец результата работы программы:
    Числа: [1, 3, 4, 16]
    Строки: ['Mouse', 'Keyboard']
Условия:
Дан список разных данных:
    ["Desktop", 16, "Mouse", 2, "Keyboard", 4, 1, 3]

Задача: Разделите данные на числа и строки с помощью isinstance()
"""

# mixed_data = ["Desktop", 16, "Mouse", 2, "Keyboard", 4, 1, 3]
#
# numbers = []
# strings = []
#
# # Для каждого объекта в mixed_data
# for item in mixed_data:
#     # Если является числом, то
#     if isinstance(item, (int, float)):
#         numbers.append(item) # вносим в список numbers
#     # Если является строкой, то
#     elif isinstance(item, str):
#         strings.append(item) # вносим в список strings
#
# print(f"Числа: {sorted(numbers)}")  # сортирует по возрастанию
# print(f"Строки: {sorted(strings)}") # сортирует по алфавиту


"""
Задание 9. Сложная фильтрация с any() и all()

Образец результата работы программы:
    Студенты, сдавшие все экзамены: ['Alice', 'Charlie']
    Студенты, сдавшие хотя бы один экзамен: ['Alice', 'Bob', 'Charlie']

Условия:
Дан словарь с результатами экзаменов:
    students = {
        "Alice": [True, True, True],
        "Bob": [False, True, False],
        "Charlie": [True, True, True],
        "David": [False, False, False]
    }

Задача: Используйте any() и all() для фильтрации
"""

# students = {
#     "Alice": [True, True, True],
#     "Bob": [False, True, False],
#     "Charlie": [True, True, True],
#     "David": [False, False, False]
# }
#
# # Студенты, сдавшие все экзамены
# passed_all = []
# for name, results in students.items():
#     # Проверяем, что всё было сдано
#     if all(results):
#         passed_all.append(name)
#
# # Студенты, сдавшие хотя бы один экзамен
# passed_any = []
# for name, results in students.items():
#     # Проверяем, что хотя бы одно было сдано
#     if any(results):
#         passed_any.append(name)
#
# print(f"Студенты, сдавшие все экзамены: {passed_all}")
# print(f"Студенты, сдавшие хотя бы один экзамен: {passed_any}")


"""
Задание 10. Комплексная задача: система валидации данных

Образец результата работы программы:
    Валидные пользователи: ['user1', 'user3']
    Невалидные пользователи: ['user2']

Условия:
    Дан список пользователей с данными:
        users = [
            {"username": "user1", "age": 25, "email": "user1@example.com", "active": True},
            {"username": "user2", "age": 15, "email": "invalid_email", "active": True},
            {"username": "user3", "age": 30, "email": "user3@example.com", "active": False}
        ]

Критерии валидности:
    Возраст >= 18
    Email содержит '@'
    Активен (active = True)

Задача: Используйте all() и any() для проверки условий
"""

# users = [
#     {"username": "user1", "age": 25, "email": "user1@example.com", "active": True},
#     {"username": "user2", "age": 15, "email": "invalid_email", "active": True},
#     {"username": "user3", "age": 30, "email": "user3@example.com", "active": False}
# ]
#
# valid_users = []
# invalid_users = []
#
# for user in users:
#     # Прописываем условия
#     conditions = [
#         user["age"] >= 18,
#         "@" in user["email"],
#         user["active"] == True
#     ]
#
#     # Проверяем все условия с помощью all()
#     if all(conditions):
#         # Если всё возвращает значение true, то:
#         valid_users.append(user["username"]) # Обновляем список пользователей,
#                                              # которые успешно прошли валидацию
#     # Иначе:
#     else:
#         invalid_users.append(user["username"]) # Обновляем список пользователей,
#                                                # которые не прошли валидацию (наверняка они боты!)
#
# print(f"Валидные пользователи: {valid_users}")
# print(f"Невалидные пользователи: {invalid_users}")


"""
Дополнительная задача повышенной сложности

Система оценки студентов

Задача: Напишите программу, которая:
    Принимает оценки студента по разным предметам
    Определяет статус студента
    Использует тернарные операторы, any/all, isinstance

Критерии:
    Отличник: все оценки >= 4.5
    Хорошист: все оценки >= 3.5 и хотя бы одна >= 4.5
    Троечник: все оценки >= 3
    Неуспевающий: есть оценки < 3
"""

def evaluate_student(grades):
    """
    Оценивает статус студента на основе оценок
    """
    # Проверяем, что все элементы - числа
    if not all(isinstance(grade, (int, float)) for grade in grades):
        return "Ошибка: не все оценки являются числами"

    # Определяем статус с помощью условий и any()/all()
    status = (
        "Отличник" if all(grade >= 4.5 for grade in grades) else
        "Хорошист" if all(grade >= 3.5 for grade in grades) and any(grade >= 4.5 for grade in grades) else
        "Троечник" if all(grade >= 3 for grade in grades) else
        "Неуспевающий"
    )

    # NB! Используйте название переменной status для результата
    return status

# Тестируем
test_grades = [
    [5, 5, 5],      # Отличник
    [4, 5, 4],      # Хорошист
    [3, 3, 4],      # Троечник
    [2, 4, 3],      # Неуспевающий
    [4.5, 4.5, 4.5] # Отличник
]

for grades in test_grades:
    result = evaluate_student(grades)
    print(f"Оценки: {grades} -> {result}")
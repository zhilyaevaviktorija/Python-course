data = "программирование"
print(tuple(data))

hse_coordinates = (59.923040, 30.303444)
temperature = (37.0, 49.5, 12.1)
user_id = (321463, 482754, 926749)

text = 'university'
set(text)
list(text)
tuple(text)

print(set(text))
print(list(text))
print(tuple(text))


"""
Задачи на синтаксис списков
"""

numbers = [10, 20, 30]
# 1. Добавьте число 40 в конец
numbers.append(40)
# 2. Удалите число 20
numbers.pop(1)
# 3. Вставьте число 5 на начало списка
numbers.insert(0, 5)
# Выведите результат
print(numbers)

"""
Кортеж
"""

rgb = (255, 128, 0)
# 1. Выведите второй элемент кортежа
print(rgb[1])
# 2. Попробуйте изменить первый элемент на 200
# rgb[0] = 200
# 3. Объясните, какая ошибка возникла
# TypeError: 'tuple' object does not support item assignment

"""
Множество
"""

# Дано:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Найдите:
# 1. Общие элементы (пересечение)
both_set = set1 & set2
# 2. Все уникальные элементы (объединение)
all_set = set1 | set2
# 3. Элементы, которые есть в set1, но нет в set2
unique_set = set1 - set2
print(f"both_set", '\n' "all_set", '\n' "unique_set")


"""
Создайте программу, которая раскидывает элементы по типам в разные списки,
т.е. создает отдельные списки для: int, str, list, tuple
"""

mixed_data = [
    1,
    "hello",
    3.14,
    [1, 2],
    42,
    "world",
    0,
    (5, 6),
    {"name": "John"},
    True,
    {7, 8, 9}
]

int_list = []
str_list = []
list_list = []
tuple_list = []
float_list = []
set_list = []
bool_list = []
other_list = []

for item in mixed_data:
   if isinstance(item, bool):
       (bool_list.append(item))
   elif isinstance(item, int):
       (int_list.append(item))
   elif isinstance(item, str):
       (str_list.append(item))
   elif isinstance(item, list):
       (list_list.append(item))
   elif isinstance(item, tuple):
       (tuple_list.append(item))
   elif isinstance(item, float):
       (float_list.append(item))
   elif isinstance(item, set):
       (set_list.append(item))
   else:
       (other_list.append(item))

print(f"Целые числа: {int_list} \n Строки: {str_list} \n"
      f"Списки: {list_list} \n Кортежи: {tuple_list} \n"
      f"Дробные числа: {float_list} \n Множества: {set_list} \n"
      f"Логические значения: {bool_list} \n Другое: {other_list}")


"""
Цикл while
"""

"""
Задача 1. Напишите цикл while, который выводит числа от 1 до 5
"""

x = 0
while x <=4:
    x +=1
    print(x)

"""
Задача 2. Напишите цикл, который принимает на вход любое слово 
и делит его на буквы (и выводит список букв на экран),
цикл остановится, если пользователь ввёл “стоп”
"""

while True:
    word = input("Введите слово (или 'стоп' для выхода): ").strip()

    if word.lower() == "стоп":
        print("Программа завершена.")
        break

    letters = list(word)
    print(f"'{word}' состоит из: {letters}")

"""
Задача 3. Реализуйте механизм входа с 3 попытками
"""

correct_password = "secret123"
logged_in = False
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    password = input("Введите пароль: ")
    attempts += 1

    if password == correct_password:
        logged_in = True
        print("Пользователь авторизован успешно")
        break
    else:
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Введите пароль заново. Осталось попыток: {remaining_attempts}")
        else:
            print("Лимит попыток исчерпан. Доступ запрещен")
# Блок 1. Регулярные выражения
print ("_" * 60)
print("Блок 1. Регулярные выражения")

import re

n = 0

# Task 1. Напишите регулярное выражение для проверки email адреса
# Программа возвращает True/False в переменную result

test_email = "test@example.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
result = bool(re.match(email_pattern, test_email))
print(result)

assert result == True, "Email должен быть валидным"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 2. Найдите все числа в строке с помощью регулярных выражений
# Программа возвращает список чисел в переменную numbers

text_with_numbers = "У меня 5 яблок и 3 апельсина"
numbers = re.findall(r'\d+', text_with_numbers)
print(numbers)

assert numbers == ['5', '3'], f"Найдены числа: {numbers}, ожидалось: ['5', '3']"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 3. Замените все числа в тексте на букву 'X'
# Программа возвращает измененную строку в переменную result

text_to_replace = "У меня 5 яблок и 3 апельсина"
result = re.sub(r'\d+', 'X', text_to_replace)
print(result)

assert result == "У меня X яблок и X апельсина", f"Результат: '{result}'"
n += 1
print(f"Решено правильно {n} задач из 18")


# Блок 2. Методы строк
print ("_" * 60)
print("Блок 2. Методы строк")

# Task 4. Выполните основные операции со строками
# Программа должна создать четыре переменные:
# upper_result, lower_result, length, words

test_string = "Hello World"

upper_result = test_string.upper()
print(upper_result)

lower_result = test_string.lower()
print(lower_result)

length = len(test_string)
print(length)

words = test_string.split()
print(words)

assert upper_result == "HELLO WORLD", "upper() не работает"
assert lower_result == "hello world", "lower() не работает"
assert length == 11, "len() не работает"
assert words == ["Hello", "World"], "split() не работает"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 5. Получите указанные части строки с помощью срезов
# Программа должна создать две переменные:
# first_part, last_part

text = "Hello World"

first_part = text[:5]
print(first_part)

last_part = text[6:]
print(last_part)

assert first_part == "Hello", f"Первая часть: '{first_part}'"
assert last_part == "World", f"Последняя часть: '{last_part}'"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 6. Создайте строку с использованием f-строк
# Программа должна создать строку в переменную formatted_string

name = "Alice"
age = 25

string_age = str(age)
formatted_string = f"Меня зовут {name} и мне {string_age} лет"
print(formatted_string)

assert formatted_string == "Меня зовут Alice и мне 25 лет", f"Результат: '{formatted_string}'"
n += 1
print(f"Решено правильно {n} задач из 18")


# Блок 3. Арифметические операции
print ("_" * 60)
print("Блок 3. Арифметические операции")

# Task 7. Выполните основные арифметические операции
# Программа должна создать семь переменных:
# addition для сложения чисел 5 и 3
# subtraction для вычитания 4 из 10
# multiplication для умножения 15 на 3
# division для деления 15 на 3
# floor_division для целочисленного деления 15 на 3
# modulo для получения остатка от деления 7 на 3
# exponent для возведения 2 в степень числа 3

addition = 5 + 3
print(addition)

subtraction = 10 - 4
print(subtraction)

multiplication = 15 * 3
print(multiplication)

division = 15 / 3
print(division)

floor_division = 15 // 3
print(floor_division)

modulo = 7 % 3
print(modulo)

exponent = 2 ** 3
print(exponent)

assert addition == 8, "Сложение не работает"
assert subtraction == 6, "Вычитание не работает"
assert multiplication == 45, "Умножение не работает"
assert division == 5.0, "Деление не работает"
assert floor_division == 5, "Целочисленное деление не работает"
assert modulo == 1, "Остаток от деления не работает"
assert exponent == 8, "Возведение в степень не работает"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 8. Продемонстрируйте работу приоритет операций с использованием скобок:
# Сложите 2 с результатом умножения 3 и 4.
# Затем сложите 2 и 3, умножив результат на 4.
# Программа должна создать две переменные: result1, result2

x = 2
y = 3
z = 4

result1 = (y * z) + x
print(result1)

result2 = (x + y) * z
print(result2)

assert result1 == 14, f"Результат1: {result1}"
assert result2 == 20, f"Результат2: {result2}"
n += 1
print(f"Решено правильно {n} задач из 18")


# Блок 4. Типы данных
print("_" * 60)
print("Блок 4. Типы данных")

# Task 9. Определите типы следующих значений: 5, 3.14, "text", [1, 2, 3], True.
# Программа должна создать пять переменных:
# type_int, type_float, type_str, type_list, type_bool

type_int = type(5)
print(type_int)

type_float = type(3.14)
print(type_float)

type_str = type("text")
print(type_str)

type_list = type([1, 2, 3])
print(type_list)

type_bool = type(True)
print(type_bool)

assert type_int == int, "Целые числа не распознаны"
assert type_float == float, "Дробные числа не распознаны"
assert type_str == str, "Строки не распознаны"
assert type_list == list, "Списки не распознаны"
assert type_bool == bool, "Булевы значения не распознаны"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 10. Преобразуйте значения между типами:
# "5" к виду целого числа, 123 к виду строки, "3.14" к виду числа с плавающей точкой.
# Программа должна создать три переменные:
# str_to_int, int_to_str, str_to_float

str_to_int = int("5")
print(type(str_to_int))

int_to_str = str(123)
print(type(int_to_str))

str_to_float = float("3.14")
print(type(str_to_float))

assert str_to_int == 5, "Преобразование строки в int не работает"
assert int_to_str == "123", "Преобразование int в строку не работает"
assert str_to_float == 3.14, "Преобразование строки в float не работает"
n += 1
print(f"Решено правильно {n} задач из 18")


# Блок 5. Присваивание переменных
print("_" * 60)
print("Блок 5. Присваивание переменных")

# Task 11. Измените значение переменной
# Создайте переменную y со значением 15.
# Программа должна изменить значение переменной x на 15 # путем перезаписи значения переменной

y = 15
x = 10
x = y
print(x)

assert x == 15, f"x = {x}, ожидалось 15"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 12. Создайте несколько переменных с числами 1, 2 и 3 одной строкой кода.
# Программа должна создать три переменные: a, b, c

a, b, c = 1, 2, 3
print(a, b, c)

assert a == 1 and b == 2 and c == 3, f"a={a}, b={b}, c={c}"
n += 1
print(f"Решено правильно {n} задач из 18")


# Блок 6. Логические операции
print("_" * 60)
print("Блок 6. Логические операции")

# Task 13. Используйте операторы сравнения
# Программа должна создать шесть переменных для проверки работы логических выражений на примере чисел 5 и 3:
# greater, less, equal, not_equal, greater_equal, less_equal

greater = 5 > 3
less = 5 < 3
equal = 5 == 3
not_equal = 5 != 3
greater_equal = 5 >= 3
less_equal = 5 <= 3

assert greater == True, "> не работает"
assert less == False, "< не работает"
assert equal == False, "== не работает"
assert not_equal == True, "!= не работает"
assert greater_equal == True, ">= не работает"
assert less_equal == False, "<= не работает"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 14. Создайте сложное логическое выражение
# Программа должна создать переменную can_drive (если пользователь старше 18)

age = 25
has_license = True

can_drive = ((age >= 18) and has_license)

assert can_drive == True, f"can_drive = {can_drive}"
n += 1
print(f"Решено правильно {n} задач из 18")


# Блок 7. Индексация
print("_" * 60)
print("Блок 7. Индексация")

# Task 15. Индексация строк - получение первого, третьего и последнего символа слова по индексам
# Программа должна создать три переменные: first_char, third_char, last_char

text = "Python"

first_char = text[0]
print(first_char)

third_char = text[2]
print(third_char)

last_char = text[-1]
print(last_char)

assert first_char == "P", f"first_char = '{first_char}', ожидалось 'P'"
assert third_char == "t", f"third_char = '{third_char}', ожидалось 't'"
assert last_char == "n", f"last_char = '{last_char}', ожидалось 'n'"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 16. Срезы строк - получение подстрок
# Программа должна создать три переменные:
# first_two (первые 2 символа), last_three (последние 3),
# middle (3 символа посередине: используйте отрицательное индексирование)

text = "Programming"

first_two = text[:2]
print(first_two)

last_three = text[-3:]
print(last_three)

middle = text[3:-4]
print(middle)

assert first_two == "Pr", f"first_two = '{first_two}', ожидалось 'Pr'"
assert last_three == "ing", f"last_three = '{last_three}', ожидалось 'ing'"
assert middle == "gram", f"middle = '{middle}', ожидалось 'gram'"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 17. Индексация списков - доступ к элементам
# Программа должна создать три переменные:
# first_item (первый элемент списка), last_item (последний элемент списка), middle_item (центральный элемент)

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

central_index = round(len(fruits)/2)

first_item = fruits[0]
print(first_item)
last_item = fruits[-1]
print(last_item)
middle_item = fruits[central_index]
print(middle_item)

assert first_item == "apple", f"first_item = '{first_item}', ожидалось 'apple'"
assert last_item == "kiwi", f"last_item = '{last_item}', ожидалось 'kiwi'"
assert middle_item == "orange", f"middle_item = '{middle_item}', ожидалось 'orange'"
n += 1
print(f"Решено правильно {n} задач из 18")


# Task 18. Срезы списков - получение подсписков
# Программа должна создать три переменные:
# first_three (последние три элемента), last_two (первые два), middle_three (три посредине)

numbers = [10, 20, 30, 40, 50, 60, 70]

first_three = numbers[:3]
print(first_three)
last_two = numbers[-2:]
print(last_two)
middle_three = numbers[2:5]
print(middle_three)

assert first_three == [10, 20, 30], f"first_three = {first_three}, ожидалось [10, 20, 30]"
assert last_two == [60, 70], f"last_two = {last_two}, ожидалось [60, 70]"
assert middle_three == [30, 40, 50], f"middle_three = {middle_three}, ожидалось [30, 40, 50]"
n += 1
print(f"Решено правильно {n} задач из 18")
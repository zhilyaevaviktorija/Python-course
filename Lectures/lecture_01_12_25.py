"""
Задачи на range
"""

"""
Задача 1. Создайте списки с помощью list(range()):
    Числа от 0 до 9
    Четные числа от 2 до 20
    Числа от 10 до 1 в обратном порядке
"""

numbers = list(range(0, 10))
even_numbers = list(range(2, 21, 2))
reverse_numbers = list(range(10, 0, -1))

print(f"Числа от 0 до 9: {numbers} \n Четные числа от 2 до 20: {even_numbers}"
      f"\n Числа от 10 до 1 в обратном порядке: {reverse_numbers}")

"""
Задача 2. Дан список слов
Найдите все слова, содержащие букву 'а', и замените их на "FOUND"
"""

words = ["apple", "banana", "cherry", "date", "fig", "grape"]

for i in range(len(words)):
    if 'a' in words[i]:
        words[i] = 'FOUND'

print(words)


"""
Задача 3. У вас есть данные о продажах: товары, цены и количество проданных единиц
Рассчитайте общую выручку по каждому товару и найдите товар с максимальной выручкой
"""

products = ["Ноутбук", "Мышь", "Клавиатура", "Монитор"]
prices = [50000, 2500, 4000, 30000]
quantities = [8, 45, 25, 12]

# Создаем хранилище для подсчета общей стоимости товаров
# новый список:
#   - Ноутбук (задается как индекс 0): prices[0] * quantities[0] -> 50000 * 8
#   - Product[i]: prices[i] * quantities[i]

final_results = [] # хранилище, куда запишутся все значения общей выручки

# начинаем итерацию с range, чтобы
# Ноутбук -> 0; Мышь -> 1 ...
for i in range(len(products)):
    # дебаг
    print(f'Товар под номером {i} -> {products[i]}')
    # вычисление общей выручки
    final = prices[i] * quantities[i]
    # как происходят вычисления: дебаг
    print(f'Цена товара {prices[i]} умножается на его количество {quantities[i]}')
    print(f'Общая выручка составит {final}')
    final_results.append(final) # Обновляем хранилище всех значений общей выручки

print("Выручка по каждому товару:", final_results)

max_revenue = max(final_results) # выводим максимальное значение из списка final_results
print("Максимальная выручка в списке:", max_revenue)

# index используется для вывода индекса данного значения в списке
# получаем индекс для max_revenue в final_results
# list.index(item)
max_index = final_results.index(max_revenue)

print("Товар с максимальной выручкой:", products[max_index])

# если мы не знаем index:
for i in range(len(products)):
    # сопоставление по индексу и значению, но вручную
    if final_results[i] == max_revenue:
        print('Товар с максимальной выручкой (поиск без list.index()):', products[i])

"""
Задача 4. В интернет-магазине нужно применить скидки к товарам,
обновить цены и пересчитать остатки (просто вывести значение stock по индексу)
"""

products = ["Телефон", "Планшет", "Ноутбук", "Наушники"]
prices = [30000, 45000, 80000, 15000]
stock = [15, 8, 5, 20]
discounts = [10, 15, 20, 5]  # Скидки в процентах

for i in range(len(products)):
    prices[i] = int(prices[i] * (100 - discounts[i]) / 100)

    print(f"Товар: {products[i]}")
    print(f"Цена со скидкой {discounts[i]}%: {prices[i]} руб.")
    print(f"Остаток на складе: {stock[i]} шт.")


# enumerate для: нумерации, логирования, создания отчетов с порядковыми номерами

fruits = ["apple", "banana", "cherry"]
print("Фрукты в корзине:")
# выведите 1. apple и т.д.

for number, fruits in enumerate(fruits, start=1):
    print(f"{number}. {fruits}")


# Синтаксис list comprehension
"""
Задача 1
[expression for item in iterable if condition]
Создайте список четных чисел от 0 до 20 двумя способами
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""

# вариант 1
even_number_list_1 = list(range(2, 21, 2))
print(f"Список четных чисел (вариант 1): {even_number_list_1}")

# вариант 2
even_number_list_2 = [x for x in range(21) if x % 2 == 0]
print(f"Список четных чисел (вариант 2): {even_number_list_2}")

"""
Задача 2. Дан список слов
Создайте список их длин (feature engineering) двумя способами
"""

words = ["python", "data", "science", "list"] # [6, 4, 7, 4]

# вариант 1
list_length_1 = []
for word in words:
    list_length_1.append(len(word))

print(f"Длина слов (вариант 1): {list_length_1}")

# вариант 2
list_length_2 = [len(word) for word in words]
print(f"Длина слов (вариант 2): {list_length_2}")

"""
Задача 3. Создайте список слов длиннее 4 символов с list comprehension
"""

words = ["cat", "elephant", "dog", "butterfly", "ox"] # ['elephant', 'butterfly']
animals_list = [word for word in words if len(word) >= 4]
print(f"Слова длиннее 4 символов: {animals_list}")

"""
Задача 4
1. Создаем пустой список numbers 
2. Начинаем while
3. Запрашиваем список чисел вида '1 2 10 -1'
4. split по пробелу
5. Фильтруем (list comp.) отрицательные и нецелые
6. Обновляем numbers 
7. Цикл завершается, если пользователь ввел 0
8. В конце выводим numbers
"""

numbers = []
while True:
    user_input = input("Введите целые числа (0 для завершения): ")

    filtered_numbers = []
    for part in user_input.split():
        try:
            num = float(part)

            # Проверяем, не является ли число 0
            if num == 0:
                break  # Выходим из цикла for

            # Фильтруем неотрицательные и целые числа
            if num >= 0 and num.is_integer():
                filtered_numbers.append(int(num))
        except:
            continue  # Пропускаем нечисловые значения

    if "0" in user_input.split():
        numbers.extend(filtered_numbers)
        break

    numbers.extend(filtered_numbers)
    print(f"Добавлены числа: {filtered_numbers}, '\n' Всего: {len(numbers)}")

print(f"Полученный результат: {numbers}")
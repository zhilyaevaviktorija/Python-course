print ("_" * 60)
print("Задание 1")

# 1. Угадай число
import random # библиотека для генерации случайных чисел

# генерируем случайное целое число (random integer) от 0 до 10
# функция randint принимает два аргумента: диапазон генерации
magic_number = random.randint(0, 10)

# запросите у пользователя ввод числа
user_number = int(input("Введите число от 0 до 10: "))

if user_number == magic_number: # проверка на совпадение значений
  print('Поздравляю, вы угадали!')
else:
  print('А вот и нет! Это число', magic_number)


print ("_" * 60)
print("Задание 2")

# 2. Приветствие
# запросите у пользователя его имя
user_name = input("Введите ваше имя: ")

# выведите на экран любое приветствие для пользователя
greeting = f"Приветствую, {user_name}!"
print(greeting)
print("_" * 60)


print ("_" * 60)
print("Задание 3")

# 3. Конвертер температур
# запросите у пользователя температуру в градусах Цельсия:
# это должно быть дробное числом (float)
celsius = float(input("Введите температуру в градусах Цельсия: "))

# конвертируйте температуру из градусов Цельсия в градусы Фаренгейта:
fahrenheit = 9/5 * celsius + 32

# выведите результат на экран:
result = f"{celsius}°C = {fahrenheit}°F"
print(result)


print ("_" * 60)
print("Задание 4")

# 4. Округление и вывод с помощью новой строки
# округлите оба значения температур в градусах Цельсия и в градусах Фаренгейта
# вы можете преобразовать результат к виду целого числа с помощью int(n); n - число для преобразования
celsius_int = int(celsius)
fahrenheit_int = int(fahrenheit)
result_int = f"Целые числа: {celsius_int}°C = {fahrenheit_int}°F"
print(result_int)

# либо воспользоваться функцией round(n, k), указав в аргументах функции количество знаков после запятой k
celsius_rounded_1 = round(celsius, 1)
fahrenheit_rounded_1 = round(fahrenheit, 1)
result_rounded_1 = f"Округление до 1 знака: {celsius_rounded_1}°C = {fahrenheit_rounded_1}°F"
print(result_rounded_1)

celsius_rounded_2 = round(celsius, 2)
fahrenheit_rounded_2 = round(fahrenheit, 2)
result_rounded_2 = f"Округление до 2 знаков: {celsius_rounded_2}°C = {fahrenheit_rounded_2}°F"
print(result_rounded_2)

# другой вариант вывода двух чисел в одну строку кода
print(str(celsius_int) + "°C" + " = " + str(fahrenheit_int) + "°F")


print ("_" * 60)
print("Задание 5")

# 5. Конвертирование типов данных

# преобразуйте округленные значения температур к виду строк, применив str(n),
# где n - то, что вы хотите преобразовать к виду строки
celsius_str = str(celsius_int)
fahrenheit_str = str(fahrenheit_int)
print(celsius_str + "°C" + " = " + fahrenheit_str + "°F") # код похож на последний вариант кода в задании 4


print ("_" * 60)
print("Задание 6")

# 6. Калькулятор

# запросите у пользователя 2 целых числа
User_number_1 = int(input("Введите первое целое число: "))
User_number_2 = int(input("Введите второе целое число: "))

# выполните операции сложения, вычитания, умножения и возведения каждого из чисел во вторую степень
addition = User_number_1 + User_number_2
subtraction = User_number_1 - User_number_2
multiplication = User_number_1 * User_number_2
exponentiation_1 = User_number_1 ** 2
exponentiation_2 = User_number_2 ** 2

# выведите результат на экран
result_2 = f"Сумма чисел: {addition}, Разность чисел: {subtraction}, Произведение чисел: {multiplication}, Вторая степень числа 1: {exponentiation_1}, Вторая степень числа 2: {exponentiation_2}"
print(result_2) # вариант 1
print("Сумма чисел:", addition, "\n" "Разность чисел:", subtraction, "\n" "Произведение чисел:", multiplication, "\n" "Вторая степень числа 1:", exponentiation_1, "\n" "Вторая степень числа 2:", exponentiation_2) # вариант 2


print ("_" * 60)
print("Задание 7")

# 7. Анкета

# используйте множественное присваивание, чтобы одной строчкой кода запросить у пользователя имя, возраст и профессию
user_name, user_age, user_profession = input("Введите ваше имя: "), input("Введите ваш возраст: "), input("Введите вашу профессию: ")

# выведите на экран полученную информацию
print("Имя:", user_name)
print("Возраст:", user_age)
print("Профессия:", user_profession)


print ("_" * 60)
print("Задание 8")

# 8. Поменять местами переменные

# запросите у пользователя две любые переменные
colour_1, colour_2 = input("Введите первый цвет: "), input("Введите второй цвет: ")

# поменяйте их местами одной строчкой кода
colour_1, colour_2 = colour_2, colour_1

# запишите в первую переменную информацию из второй, а во вторую переменную - информацию из первой, используя множественное присваивание
print("Первый цвет:", colour_1)
print("Второй цвет:", colour_2)


print ("_" * 60)
print("Задание 9")

# 9. Дописать функцию

def sum_and_product(a, b):
    # напишите здесь код для расчета суммы чисел a и b
    total_sum = a + b
    # а сюда допишите код для подсчета их произведения
    product = a * b
    # функция возвращает результат подсчета - два новых числа
    return total_sum, product

# мы вызываем функцию sum_and_product и передаем ей в качестве аргументов два числа - 5 и 3
# мы помним, что функция возвращает 2 новых числа, поэтому результат работы одной функции мы записываем в две переменные: result_sum и result_product
result_sum, result_product = sum_and_product(5, 3)

# выведите на экран result_sum и result_product
print(result_sum, result_product)


print ("_" * 60)
print("Задание 10")

# 10. Строка и число

# запросите у пользователя 2 числа, используйте str(input())
user_num_1, user_num_2 = str(input("Введите первое число: ")), str(input("Введите второе слово: "))

# сложите два числа, не меняя тип данных, и выведите на экран результат
sum_str = user_num_1 + user_num_2

# преобразуйте числа к виду нужного типа и снова сложите их, выведите результат
sum_int = int(user_num_1) + int(user_num_2)
print(sum_str, sum_int)
num1 = 10
num2 = 20

# Написала код для сложения 2-х чисел.

result =  num1 + num2
print(result)

# Написала код для вычитания 2-х чисел.

result =  num1 - num2
print(result)

# Написала код для умножения 2-х чисел.

result =  num1 * num2
print(result)

# Написала код для деления 2-х чисел.

result =  num1 / num2
print(result)

str1 = "Hello, "
str2 = "World!"

# Написала код для сложения 2-х строк.
# Получилась строка "Hello, World!".

result =  str1 + str2

print(result)

str1 = "Hello, "
num1 = 10

# Написала код для сложения строки и числа.
# Получилась ошибка (несовпадение типов).
# Ввела функцию str.

result =  str1 + str(num1)

print(result)

str1 = "Hello, "
num1 = "10"

# Написала код для сложения строки и числа.
# Сложение одинаковых типов.

result =  str1 + num1

print(result)

num1 = 10
num2 = 20

# Сложение 2-х чисел с помощью оператора +=.

num1 += num2

print(num1)

num1 = 10
num2 = 20

# Вычитание 2-х чисел с помощью оператора -=.

num1 -= num2

print(num1)

num1 = 10
num2 = 20

# Умножение 2-х чисел с помощью оператора *=.

num1 *= num2

print(num1)

num1 = 10
num2 = 20

# Деления 2-х чисел с помощью оператора /=.

num1 /= num2

print(num1)

# ========Практика перед новым занятием===========

# 1: создай переменную с именем user_age и сохрани в ней число, введённое с клавиатуры.
user_age = int(input("Введи свой возраст: "))

# Проверка
assert isinstance(user_age, int)
print("Переменная создана правильно.")

# Теперь введи сюда имя пользователя
user_age = input("Введи имя: ")

# Проверка
assert isinstance(user_age, str)

# Получилась ошибка, т.к. нельзя преобразовать строку в число.


# Задания на закрепление материала
#1. Создала переменную x = 10 и прибавила к ней 5 с помощью сокращённого (комбинированного) оператора.

x = 10
x+=5
print(x)

#2. Написала код, чтобы преобразовать температуру в градусах по Цельсию к виду значений температуры в градусах по Фаренгейту. Использовать int(input()) для ввода значения температур.
celsey = int(input("Введите температуру в градусах по Цельсию: "))
print(celsey*1.8+32)

#3. Написала код, чтобы переводить минуты в часы и считать остаток минут. Использовала int(input()) для ввода количества минут.
minute = int(input("Введите количество минут: "))
hour = minute//60
minute = minute%60
print('hour: ' + str(hour), 'minute: ' + str(minute))

#4. Ячейка кода ниже должна принимать 2 числа и считать их сумму, разность, произведение и частное.
num1 = int(input("Впишите первое число: "))
num2 = int(input("Впишите второе число: "))

def summation(n1, n2):
    return n1 + n2
print(summation(num1, num2))

def substraction(n1, n2):
    return n1 - n2
print(substraction(num1, num2))

def multiplication(n1, n2):
    return n1 * n2
print(multiplication(num1, num2))

def division(n1, n2):
    return n1 / n2
print(division(num1, num2))

#5. Сколько будет 15% от 200?
print((200*15)/100)
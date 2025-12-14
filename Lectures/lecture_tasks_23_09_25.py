# Задача 1. Форматирование ФИО
full_name = "иванов иван иванович"
surname, name, patronymic = full_name.split()
result = f"{surname.title()} {name[0].upper()}.{patronymic[0].upper()}."
print(result)
# Ожидаемый вывод: "Иванов И.И."

# Задача 2. Анализ пароля
password = "Password123"
print(len(password))
# Проверьте:
# - длину не менее 8 символов
# - содержит цифры
# - содержит заглавные буквы
length_ok = len(password) >= 8
has_digits = any(char.isdigit() for char in password)  # упрощенная проверка
has_upper = password != password.lower()
print(f"Длина OK: {length_ok}")
print(f"Есть цифры: {has_digits}")
print(f"Есть заглавные: {has_upper}")

# Задача 3. Обработка пути к файлу
path = "/home/user/documents/report.pdf"
# Извлеките имя файла без расширения
filename = path.split("/")[-1]
filename_2 = filename.split(".")[0]
print("Имя файла без расширения: " + filename_2)
# Ожидаемый вывод: "report"

# Задача 4. Поиск телефона
import re
text = "Звоните по номеру +7-123-456-78-90 или +7-987-654-32-10"
# Найдите все номера телефонов (содержат +7-)
phone_num = re.findall(r'\+\d-\d{3}-\d{3}-\d{2}-\d{2}', text)
print(phone_num)

# Задача 5. Нормализация текста
text_1 = "   ЭТОТ ТЕКСТ ПИСАЛИ КАПСОМ    "
# Приведите к нормальному виду: первая буква заглавная, остальные маленькие
# Вариант 1
clean_text_1 = text_1.strip()
text_1_first_letter = clean_text_1[:1]
lower_text = clean_text_1[1:].lower()
print(text_1_first_letter + lower_text)
# Вариант 2
text_2 = "   ЭТОТ ТЕКСТ ПИСАЛИ КАПСОМ    "
normalized_text = text_2.strip().lower().capitalize()
print(normalized_text)
# Ожидаемый вывод: "Этот текст писали капсом"

# Задача 6: Подсчет слов
sentence = "Быстрый рыжий лис прыгает через ленивую собаку"
# Посчитайте количество слов в предложении
words = sentence.split(" ")
print(len(words))
# Ответ: 7

# Задача 7: Замена даты
text_2 = "Встречаемся 2023-12-31 в 20:00"
# Замените формат даты на 31.12.2023
# Вариант 1
new_text = text_2.replace("2023-12-31", "31.12.2023")
print(new_text)  # "Встречаемся 31.12.2023 в 20:00"
# Вариант 2
import re
text_3 = "Встречаемся 2023-12-31 в 20:00"
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3.\2.\1', text_3)
print(new_text)

# Задача 8: Валидация имени файла
filename = "my_document.backup.pdf"
# Проверьте, является ли файл PDF-документом
print(filename[:-3] != "pdf")

# Задача 9: Разбор URL
url = "https://example.com/category/product.html"
# Извлеките домен и имя страницы
clean_url = url.replace("//", "/")
arr = url.split("/")
domain = arr[2]
filename = arr[-1]
filename_2 = filename.split(".")[0]
print(filename_2, domain)

# Задача 10: Генератор логина
full_name = "Maria Ivanova"
# Создайте логин в формате: m_ivanova
login = full_name[0].lower() + "_" + full_name.split()[1].lower()
print(login)
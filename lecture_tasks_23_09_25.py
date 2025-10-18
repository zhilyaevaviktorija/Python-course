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
text = "Звоните по номеру +7-123-456-78-90 или +7-987-654-32-10"
# Найдите все номера телефонов (содержат +7-)

# Задача 5. Нормализация текста
text_1 = "   ЭТОТ ТЕКСТ ПИСАЛИ КАПСОМ    "
# Приведите к нормальному виду: первая буква заглавная, остальные маленькие
clean_text_1 = text_1.strip()
text_1_first_letter = clean_text_1[:1]
lower_text = clean_text_1[1:].lower()
print(text_1_first_letter + lower_text)
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
new_text = text_2.replace("2023-12-31", "31.12.2023")
print(new_text)  # "Встречаемся 31.12.2023 в 20:00"

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
def create_login(name):
    arr = name.split(" ")
    name_login = arr[0]
    surname = arr[1]

    new_name = name_login[:1].lower() + "_" + surname.lower()
    return new_name

print(create_login(full_name))
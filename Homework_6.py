"""
Задачи на синтаксис
"""

"""
Задача 1
1. Создайте список mixed_data, содержащий:
    3 числа (int)
    2 строки (str)
    1 вложенный список
    1 кортеж
    1 множество
2. Добавьте в конец списка число 123
3. Удалите вторую строку из списка
4. Вставьте строку "inserted" на позицию 2
5. Выведите итоговый список
"""

mixed_data = [
    3,
    "Today is Monday",
    [2, 7, 12],
    ("I", "me", "my"),
    15,
    "wonderful",
    94,
    {11, 22, 33}
]
print(f"Список данных: {mixed_data}")

mixed_data.append(123)
print(f"Добавили 123: {mixed_data}")

mixed_data.pop(1)
print(f"Удалили вторую строку: {mixed_data}")

mixed_data.insert(2, "inserted")
print(f"Добавили 'inserted': {mixed_data}")

print(f"Итоговый список: {mixed_data}")

"""
Задача 2
1. Создайте кортеж user_credentials, содержащий:
    Логин (строка)
    Хэш пароля (строка)
    Уровень доступа (целое число)
2. Попробуйте изменить уровень доступа (должна возникнуть ошибка)
3. Напишите комментарий, почему кортеж подходит для хранения таких данных
"""

user_credentials = ("admin", "123456abcdef", 2)
print(f"Кортеж: {user_credentials}")
print(f"Логин: {user_credentials[0]}")
print(f"Хэш пароля: {user_credentials[1]}")
print(f"Уровень доступа: {user_credentials[2]}")

# user_credentials[2] = 3
# print(user_credentials)
# TypeError: 'tuple' object does not support item assignment
"""
Кортеж подходит для хранения учетных данных,
потому что он неизменяем и безопасен,
а также работает быстрее списков  
"""

"""
Задача 3
Дано:
    tags1 = {"python", "ml", "data"}
    tags2 = {"ml", "nlp", "deeplearning"}
Найдите:
1. Общие теги (пересечение)
2. Все уникальные теги (объединение)
3. Теги, которые есть в tags1, но нет в tags2
"""

tags1 = {"python", "ml", "data"}
tags2 = {"ml", "nlp", "deeplearning"}
both_tags = tags1 & tags2
all_tags = tags1 | tags2
unique_tags = tags1 - tags2
print(f"Общие теги: {both_tags}",
      '\n' f"Все уникальные теги: {all_tags}",
      '\n' f"Теги, которые есть в tags1, но нет в tags2: {unique_tags}")


"""
Фильтрация и обработка текстовых данных
"""

"""
1. Установите nltk и загрузите стоп-слова для русского и английского языков
"""

import nltk
import string
from nltk.corpus import stopwords

# # Установка nltk и загрузка стоп-слов
# nltk.download('stopwords')

# Загрузка стоп-слов для русского и английского языков
stopwords_english = stopwords.words('english')
stopwords_russian = stopwords.words('russian')

print(f"Исходный список английских стоп-слов: {len(stopwords_english)}")
print(f"Исходный список русских стоп-слов: {len(stopwords_russian)}")

"""
2. Конвертируйте списки слов на русском и английском, приведите их к виду множества set
Это стандартная операция: работа со стоп-словами всегда начинается с фильтрации, удаления дубликатов
"""

stopwords_english_set = set(stopwords_english)
stopwords_russian_set = set(stopwords_russian)

# Проверяем, есть ли дубликаты в исходных списках
english_duplicates = len(stopwords_english) - len(stopwords_english_set)
russian_duplicates = len(stopwords_russian) - len(stopwords_russian_set)

print(f"Дубликатов в английском списке: {english_duplicates}")
print(f"Дубликатов в русском списке: {russian_duplicates}")

"""
3. Выведите на экран первые 10 стоп-слов из двух списков
Подумайте, как это сделать, ведь set нельзя индексировать, а созданный список слов нельзя перезаписывать
"""

print("Английские стоп-слова (первые 10):", list(stopwords_english_set)[:10])
print("Русские стоп-слова (первые 10):", list(stopwords_russian_set)[:10])

"""
4. Дан текст
"""

# Исходный текст
text = """
This is a sample text for processing. It contains some stopwords and important words.
Этот текст содержит как английские, так и русские слова, включая стоп-слова.
"""

"""
Допишите функцию в указанном плейсхолдере

Функция:
    удаляет знаки препинания
    разбивает текст на слова
    приводит текст к нижнему регистру
"""

# Токенизация текста на слова
import re

def tokenize_text(text):
    text_lower = text.lower()

    # Убираем знаки препинания и разбиваем на слова
    text_clean = re.sub(r'[^\w\s]', '', text_lower)

    words = text_clean.split()

    return words

"""
Применим нашу функцию к тексту
"""

# Токенизируем текст
words = tokenize_text(text)

"""
Выведите на экран список токенов и общее количество слов
"""

print("Список токенов:", words)
print("Общее количество слов:", len(words))

"""
5. Произведите фильтрацию стоп-слов для двух языков
    Создайте пустой список
    Запустите цикл for (for word in words, для каждого слова в списке слов)
    Если слова нет в списке стоп-слов
    Сделайте append в созданный список
Допишите функцию
"""

# Фильтрация стоп-слов для обоих языков
def filter_stopwords(words, stopwords_set):
    filtered_words = []
    for word in words:
        if word not in stopwords_set:
            filtered_words.append(word)

    return filtered_words

"""
6. Примените операции со множествами
"""

# Объедините стоп-слова обоих языков в общее множество
all_stopwords = stopwords_english_set | stopwords_russian_set

"""
7. Применим нашу функцию для фильтрации данных
В переменной all_stopwords должен быть результат объединения множеств из пункта 6
"""

# Фильтруем стоп-слова
meaningful_words = filter_stopwords(words, all_stopwords)

"""
Выведите на экран список meaningful_words, а также длину этого списка
"""
print(f"Слова после фильтрации стоп-слов: {meaningful_words}", '\n',
      f"Количество слов после фильтрации: {len(meaningful_words)}")

"""
8. Создаем множество уникальных значимых слов
Конвертируем список meaningful_words к виду множества
"""

unique_meaningful_words = set(meaningful_words)

"""
Выведите на экран результат, а также длину получившегося множества
"""
print(f"Уникальные значимые слова: {unique_meaningful_words}", '\n',
      f"Количество уникальных значимых слов: {len(unique_meaningful_words)}")

"""
9. Создайте отчет
    выведите исходное количество стоп-слов на английском
    исходное количество стоп-слов на русском
    общее количество стоп-слов
"""

print(f"Всего стоп-слов (английские): {len(stopwords_english_set)}", '\n',
      f"Всего стоп-слов (русские): {len(stopwords_russian_set)}", '\n',
      f"Всего стоп-слов (объединенные): {len(all_stopwords)}")

"""
10. Проведите анализ результатов: какие стоп-слова были удалены из исходного текста?
    создайте список для сохранения отфильтрованных слов
    для каждого слова исходного текста (text),
    если данное слово было в списке стоп-слов,
    добавляем его в созданный список
Выведите на экран отфильтрованные слова (т.е. удаленные)
"""

# Создаем список для сохранения отфильтрованных стоп-слов
removed_stopwords = []

# Для каждого слова исходного текста
for word in words:
    # Если данное слово было в списке стоп-слов
    if word in all_stopwords:
        # Добавляем его в созданный список отфильтрованных слов
        removed_stopwords.append(word)

print(f"Удаленные стоп-слова: {removed_stopwords}", '\n',
      f"Количество удаленных стоп-слов: {len(removed_stopwords)}")
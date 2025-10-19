# Task 1
# В тексте найдите все цены (после слова цена или знака $).
import re

text = "Смартфон цена 29999 руб. Ноутбук $1500. Книга всего 499 рублей."
prices = re.findall(r"\d+", text)
print(prices)
assert "29999" in prices and "1500" in prices and "499" in prices

# Task 2
# Очистка HTML-тегов Удалим все HTML-теги из текста с помощью шаблона <[^>]+>
html_text = "<div>Привет, <b>мир</b>!</div>"
clean = re.sub(r"<[^>]+>", "", html_text)
print(clean)
assert clean.strip() == "Привет, мир!"

# Task 3
# Извлеките все email-адреса из текста лога.
log_text = """
2024-05-20 10:00:00 [ERROR] User ivanov_1990@domain.com: Connection timeout
2024-05-20 10:01:15 [INFO] User petrov-sergey@my-mail.org: Login successful
2024-05-20 10:02:30 [WARN] User support@company.com: Password change required
"""
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", log_text)
print(emails)
assert len(emails) == 3

# Task 4
# Извлеките номера телефонов в формате +7 (XXX) XXX-XX-XX или 8-XXX-XXX-XX-XX.
sample = "Контакты: +7 (912) 345-67-89, 8-912-345-67-89, старый формат 89123456789"
phones = re.findall(r"(?:\+7|8)[\s\-\(]*\d{3}[\)\s\-]*\d{3}[\s\-]*\d{2}[\s\-]*\d{2}", sample)
print(phones)
assert len(phones) >= 2

# Task 5
# Извлеките все URL из строки.
text = "Наш сайт: https://example.com и резервный http://backup.org/test"
urls = re.findall(r"https?://[\w./-]+", text)
print(urls)
assert "https://example.com" in urls and "http://backup.org/test" in urls

# Task 6
# Найдите даты формата YYYY-MM-DD или DD.MM.YYYY.
dates_text = "Встреча 2024-05-20 и отчёт 13.10.2025."
dates = re.findall(r"\d{4}-\d{2}-\d{2}|\d{2}\.\d{2}\.\d{4}", dates_text)
print(dates)
assert "2024-05-20" in dates and "13.10.2025" in dates
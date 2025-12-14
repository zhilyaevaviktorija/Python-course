"""
Словарь
dict()
"""

# Task 0
import json

# 1. Прочитать JSON-файл в словарь data
with open("data.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 2. Итерировать по всем ключам верхнего уровня и вывести их
print("Ключи верхнего уровня:")
for key in config.keys():
    print(f"- {key}")

# 3. Итерировать по всем значениям словаря departments
print("\n""Значения словаря departments:")
for employees in config['departments'].values():
    print(f"- {employees}")

# 4. Итерировать по парам ключ-значение в departments
print("\n""Пары ключ-значение в departments:")
for key, value in (config['departments'].items()):
    print(f"- {key}: {value}")

# 5. Добавить нового сотрудника "David" в отдел "dev"
config['departments']['dev'].append('David')
print("\n"f"David добавлен в отдел dev: {config['departments']['dev']}")

# 6. Увеличить бюджет на 10%
config["budget"] = round(config["budget"] * 1.1, 2)
print("\n""Бюджет увеличен на 10%:", config["budget"])

# 7. Записать изменённый словарь обратно в файл
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)
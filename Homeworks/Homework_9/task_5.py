"""
Задача 5: Работа с JSON-конфигом NLP-сервиса
"""

print("ЗАДАЧА 5")

import json

# 1. Загрузите конфигурацию из JSON-файла
with open('nlp_service_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 2. Добавьте новую модель для "summarization" с соответствующими параметрами
config["models"]["summarization"] = {
    "path": "/models/bart-summarization",
    "max_input_length": 1024,
    "supported_languages": ["en", "es", "de", "fr"]
}
print("\nДобавлена модель summarization:")
print(f"- путь: {config['models']['summarization']['path']}")
print(f"- макс. длина: {config['models']['summarization']['max_input_length']}")
print(f"- языки: {config['models']['summarization']['supported_languages']}")

# 3. Увеличьте rate_limit на 50%
config["rate_limit"] = int(config["rate_limit"] * 1.5)
print(f"\nПараметр rate_limit увеличен на 50%: {config['rate_limit']} запросов/сек")

# 4. Добавьте русский язык ("ru") в поддерживаемые языки для модели sentiment
if "ru" not in config["models"]["sentiment"]["supported_languages"]:
    config["models"]["sentiment"]["supported_languages"].append("ru")
    print(f"\nВ модель sentiment добавлен язык: 'ru'")
else:
    print(f"Язык 'ru' уже есть в списке")

# 5. Создайте отдельный словарь только с настройками сервера
server_config = config["server"].copy()
print("\nСоздан словарь настроек сервера:")
for key, value in server_config.items():
    print(f"- {key}: {value}")

# 6. Сохраните обновленную конфигурацию в новый файл nlp_service_config_updated.json
output_file = 'nlp_service_config_updated.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print(f"\nОбновленная конфигурация сохранена в файл: {output_file}")
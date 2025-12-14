"""
Задача 1: Анализ конфигурации модели NLP
"""

config = {
    "model_name": "bert-base-uncased",
    "batch_size": 32,
    "max_length": 128,
    "learning_rate": 2e-5,
    "epochs": 3,
    "labels": ["positive", "negative", "neutral"]
}

print("ЗАДАЧА 1")

# 1. Получите значение learning_rate двумя способами: через скобки и через get()
learning_rate_1 = config["learning_rate"]
learning_rate_2 = config.get("learning_rate")
print(f"\nПервый способ: {learning_rate_1} \nВторой способ: {learning_rate_2}")

# 2. Добавьте новый параметр "early_stopping": True
config["early_stopping"] = True
print(f"\nДобавлен параметр 'early_stopping': {config['early_stopping']}")

# 3. Измените batch_size на 64
config["batch_size"] = 64
print(f"\nПараметр batch_size изменен: {config['batch_size']}")

# 4. Пройдитесь по всем параметрам конфигурации и выведите только те, значения которых - числа
print("\nЧисловые параметры конфигурации:")
num_par = {}
for key, value in config.items():
    if isinstance(value, (int, float)):
        num_par[key] = value
        print(f"- {key}: {value} ({type(value).__name__})")

# 5. Создайте копию конфигурации для тестирования с batch_size=8 и epochs=1
test_config = config.copy()
test_config["batch_size"] = 8
test_config["epochs"] = 1
test_config["mode"] = "test"
print(f"\nКонфигурация для тестирования: {test_config}")
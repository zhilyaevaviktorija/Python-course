"""
Задача 3: Конфигурация пайплайна обработки текста
"""

pipeline_config = {
    "steps": {
        "tokenization": {"enabled": True, "method": "word"},
        "stopwords": {"enabled": True, "language": "english", "custom_words": []},
        "stemming": {"enabled": False, "algorithm": "porter"},
        "normalization": {"enabled": True, "lowercase": True, "remove_punct": True}
    },
    "input_encoding": "utf-8",
    "output_format": "tokens"
}

print("ЗАДАЧА 3")

# 1. Включите stemming, установив "enabled": True
pipeline_config["steps"]["stemming"]["enabled"] = True
print(f"\nСтемминг включен: {pipeline_config['steps']['stemming']['enabled']}")

# 2. Добавьте "numbers" в custom_words для стоп-слов
pipeline_config["steps"]["stopwords"]["custom_words"].append("numbers")
print(f'\nСлово "numbers" добавлено в список стоп-слов: '
      f'{pipeline_config["steps"]["stopwords"]["custom_words"]}')

# 3. Получите список всех включенных шагов пайплайна
print("\n""Включенные шаги пайплайна:")
enabled_steps = []
for step_name, step_config in pipeline_config["steps"].items():
    if step_config.get("enabled", False):
        enabled_steps.append(step_name)
        print(f"- {step_name}")
        # stemming добавляется в вывод, потому что мы включили его в п.1

# 4. Измените output_format на "vectors"
pipeline_config["output_format"] = "vectors"
print("\n""Поле output_format изменено на:", pipeline_config["output_format"])

# 5. Создайте упрощенную конфигурацию только с включенными шагами
simplified_config = {
    "steps": {},
    "input_encoding": pipeline_config["input_encoding"],
    "output_format": pipeline_config["output_format"]
}

# Копируем только включенные шаги
for step_name, step_config in pipeline_config["steps"].items():
    if step_config.get("enabled", False):
        simplified_config["steps"][step_name] = step_config.copy()

print("\n""Упрощенная конфигурация с включенными шагами:")
for key, value in simplified_config.items():
    if key == "steps":
        print(f"- {key}:")
        for step_name, step_config in value.items():
            print(f"- {step_name}: {step_config}")
    else:
        print(f"- {key}: {value}")
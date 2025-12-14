"""
Задача 2: Обработка ответа от NLP-сервиса
"""

api_response = {
    "text": "I really enjoyed the movie, the acting was amazing!",
    "sentiment": {
        "label": "positive",
        "score": 0.95,
        "confidence": "high"
    },
    "entities": [
        {"entity": "movie", "type": "ENTERTAINMENT", "confidence": 0.89},
        {"entity": "acting", "type": "SKILL", "confidence": 0.92}
    ],
    "language": "en",
    "processed_in": 0.45
}

print("ЗАДАЧА 2")

# 1. Получите оценку тональности (score)
score = api_response["sentiment"]["score"]
print(f"\nПолучена оценка тональности: {score}")

# 2. Пройдитесь по всем сущностям (entities) и выведите только названия сущностей
print("\nНазвание сущностей:")
entity_names = []
for entity in api_response["entities"]:
    entity_name = entity["entity"]
    entity_names.append(entity_name)
    print(f"- {entity_name}")

# 3. Найдите сущность с максимальной уверенностью (confidence)
print("\nСущность с максимальной уверенностью:")
max_confidence_entity = max(api_response["entities"],
                            key=lambda x: x["confidence"])
print(f"- сущность: {max_confidence_entity['entity']},"
      f"\n- тип: {max_confidence_entity['type']}"
      f"\n- уверенность: {max_confidence_entity['confidence']}")

# 4. Добавьте в поле ответа "model_version": "2.1.0"
api_response["model_version"] = "2.1.0"
print(f"\nДобавлена версия модели: model_version = {api_response['model_version']}")

# 5. Отфильтруйте все поля, значения которых являются строками
print("\nПоля со строковыми значениями:")
string_fields = {}
for key, value in api_response.items():
    if isinstance(value, str):
        string_fields[key] = value
        print(f"- {key}: {value}")

# Проверяем вложенные структуры
print("\nСтроковые значения во вложенных структурах:")

# sentiment словарь
for key, value in api_response["sentiment"].items():
    if isinstance(value, str):
        print(f"- sentiment.{key}: {value}")

# entities список
for i, entity in enumerate(api_response["entities"]):
    for key, value in entity.items():
        if isinstance(value, str):
            print(f"- entities[{i}].{key}: {value}")
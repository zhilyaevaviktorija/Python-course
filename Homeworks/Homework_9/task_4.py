"""
Задача 4: Агрегация статистики NLP-моделей
"""

print("ЗАДАЧА 4")

models_stats = {
    "bert-base": {
        "accuracy": 0.92,
        "f1_score": 0.91,
        "inference_time": 120,
        "size_mb": 440
    },
    "distilbert": {
        "accuracy": 0.89,
        "f1_score": 0.88,
        "inference_time": 65,
        "size_mb": 250
    },
    "roberta-large": {
        "accuracy": 0.94,
        "f1_score": 0.93,
        "inference_time": 210,
        "size_mb": 1600
    }
}

# 1. Найдите модель с максимальной точностью (accuracy)
print("\nМодель с максимальной точностью:")
# Используем max() с key для поиска по accuracy
best_model = max(models_stats.items(),
                 key=lambda item: item[1]["accuracy"])
print(f"- модель: '{best_model[0]}'")
print(f"- accuracy: {best_model[1]['accuracy']}")
print(f"- f1-score: {best_model[1]['f1_score']}")

# 2. Рассчитайте среднее время инференса по всем моделям
total_time = sum(stats["inference_time"] for stats in models_stats.values())
avg_time = total_time / len(models_stats)
print(f"\nОбщее время инференса: {total_time}")
print(f"Среднее время инференса: {avg_time:.1f}")

# 3. Создайте новый словарь только с метриками accuracy и f1_score для каждой модели
simplified_stats = {}
for model, stats in models_stats.items():
    simplified_stats[model] = {
        "accuracy": stats["accuracy"],
        "f1_score": stats["f1_score"]
    }

print("Словарь с метриками accuracy и f1_score:")
for model, metrics in simplified_stats.items():
    print(f"- {model}: accuracy={metrics['accuracy']}, f1={metrics['f1_score']}")

# 4. Добавьте новую модель "albert-base" с данными: accuracy=0.87, f1_score=0.86, inference_time=55, size_mb=180
models_stats["albert-base"] = {
    "accuracy": 0.87,
    "f1_score": 0.86,
    "inference_time": 55,
    "size_mb": 180
}
print("\nДобавлена модель: albert-base")
print(f" с параметрами: accuracy={models_stats['albert-base']['accuracy']}, "
      f"f1={models_stats['albert-base']['f1_score']}, "
      f"time={models_stats['albert-base']['inference_time']}, "
      f"size={models_stats['albert-base']['size_mb']} MB")

# 5. Отфильтруйте модели, размер которых меньше 500 МБ
print("\nМодели размером меньше 500 МБ:")
small_models = {}
for model, stats in models_stats.items():
    if stats["size_mb"] < 500:
        small_models[model] = stats

for model, stats in small_models.items():
    print(f"- {model}: {stats['size_mb']} MB "
          f"(accuracy={stats['accuracy']}, time={stats['inference_time']})")
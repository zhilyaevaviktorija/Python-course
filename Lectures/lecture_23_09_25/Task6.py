greet_text = "Привет,"
print(greet_text)

name = input("Введите имя: ")
print("Hi," + name + "!")

surname = input("Введите фамилию: ")
name += surname
print("Hi," + name + "!")

age = input("Введите возраст: ")
print("User:", name + surname, "\n", "Age:" + age)
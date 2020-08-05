# Все первые буквы строки станут заглавными .title()
mynew_string = "Привет я интерпретатор Питон"
print(mynew_string.title())

mysecond_string = "вторая Строка"
print(mysecond_string.lower())
print(mysecond_string.upper())

# Конкатинация строк
first_name = "Олег"
last_name = "Фокин"
second_name = "константинович"
full_name = f"{first_name} {last_name} {second_name}"
print(f"{full_name}")

message = f"приветствую {full_name}"
print(message.title())

# Cтарый формат
full_name2 = "{} {}".format(first_name,last_name)
print(full_name2)

# Примеры Табуляции \t Переноса строки \n
full_name = f"{last_name} \n{first_name} \n{second_name}"
print(full_name)


# Удаление пропусков rstrip удаляет все пробелы справа
# lstrip слева
# strip с обеих сторон
message_test = 'Привет я строка из python    '
message_test2 = '   Привет я строка из python    '
print(message_test.rstrip())
print(message_test2.strip())
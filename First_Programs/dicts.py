# Обработка словарей.

gamer_0 = {
    'username': 'Gvozdoder',
    'surname': 'Fokin',
    'first_name': 'Oleg',
    'last_name': 'Konstantinovich',
    'email': 'gvozdoder-92@mail.ru',
    'telephone': '8-925-321-75-68'
}

# Перебор значений.
for keys, params in gamer_0.items():
    print(f"\nКлюч: {keys}")
    print(f"Значение:{params}")

# Перебор ключей.
for keys in gamer_0.keys():
    print(f"Ключик: {keys}")



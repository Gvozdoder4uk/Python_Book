# Списки
heavy_cars = ['Kamaz', 'taiGa', 'crasher', 'azov', 'Titan']
print(heavy_cars)

# Вывод элемент списка по индексу
print(heavy_cars[0].title())

# Вывод последнего элемента списка
print(heavy_cars[-1].upper())

print(f"Мой первый купленный вездеход был {heavy_cars[0].title()}")

friends = ['oleg', 'denis', 'stepan', 'alexey']
for name in friends:
    print(f"Славный друже - {name.title()}")

# Изменени элементов в списке.
mega_cars = ['Azov', 'Taiga', 'Porshe', 'Kamaz', 'Mazda']

# Изменение элемента списка
mega_cars[2] = 'Moskvich'
print(mega_cars)

# Добавление элемента в список.
# В конец списка
mega_cars.append('Starter')
print(mega_cars)

# В произвольное место списка.
mega_cars.insert(2, 'Porshe')
print(mega_cars)

# Удаление элемента из списка.
del mega_cars[2]
print(mega_cars)
# Удаление по имени элемента
top_car = "azov"
mega_cars.remove(top_car.title())
print(f"Лучшим внедорожником признан {top_car.title()} \nДанный автомобиль более не участвует в рейтинге")

# Изьятие элемента из списка (АКА ВЫРЕЗАТЬ) удаляет из списка элемент и передает его параметры.
poped_car = mega_cars.pop()  # Last element
print(poped_car)

# Cортировка списка
mega_cars = ['Azov', 'Taiga', 'Porshe', 'Kamaz', 'Mazda']
mega_cars.sort()
print(f"Тудой - {mega_cars}")
mega_cars.sort(reverse=True)
print(f"Сюдой - {mega_cars}")

# Временная сортировка
mega_cars = ['Azov', 'Taiga', 'Porshe', 'Kamaz', 'Mazda']
print(f'Исходный список {mega_cars}')
print(f'Отсортированный {sorted(mega_cars,reverse=True)}')
# Разворот списка
mega_cars.reverse()
print(mega_cars)

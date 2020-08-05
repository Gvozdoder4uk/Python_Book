# Practice
# Приглашения на встречу, и замена не пришедшего.
important_persons = ['Bill Gates', 'Steve Jobs', 'Jeff Bezos']
for person in important_persons:
    print(f"Приглашаем {person.title()} на встречу.")
    if person.__contains__("Bill"):
        removed = person

print(f"{removed.title()} не сможет прийти")
important_persons.remove(removed)
important_persons.append("Царь")
print(f"За место него приглашен - {important_persons[-1]}")

important_persons = ['Bill Gates', 'Steve Jobs', 'Jeff Bezos', 'Просто Царь', 'Создатель World of Warcraft']
print(f"Кол-во приглашаемых = {len(important_persons)}")
for i in important_persons:
    important_persons.pop()
    if (len(important_persons) == 2):
        print("Осталось два элемента списка")
        break
print(important_persons)

last_mans_standing = len(important_persons) - 1
print(len(important_persons))
i = 0
while i <= last_mans_standing:
    print(important_persons[0])
    del important_persons[0]
    i += 1

print(important_persons)

# Циклы вывода Range
for number in range(1, 10):
    print(number)

# Генерация числового списка.
numbers = list(range(2, 11, 2))
print(numbers)

# Создание списка из квадратов всех четных чисел
squares = []
for value in range(2, 11, 2):
    square = value ** 2
    squares.append(square)
print(squares)

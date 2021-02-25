def func_one():
    animals = {'Dog', 'Tiger', 'Cat', 'Mouse', 'Cat'}
    print(len(animals))
    print(animals)


# Выводятся только уникальные элементы


def func_two():
    animals = {'Dog', 'Tiger', 'Cat', 'Mouse', 'Cat'}
    new = {"Rat", "Cat"}
    animals.update(new)
    print(animals)


# Добавление элементов в множество.


# Задачки на списки имен

def list_names() -> None:
    list_name = ['Oleg', 'Denis', 'Kate']
    get_names = ['Bob', 'Elena', 'Denis']
    new_list = list(set(list_name + get_names))  # Сложение двух списков и получение уникального
    new_list = list(set(list_name) - set(get_names))  # Уникальные элементы в левом списке.
    new_list = list(set(list_name) ^ set(get_names))  # Уникальные
    # new_list = list(set(list_name) & set(get_names))
    print(type(new_list))
    print(new_list)


if __name__ == '__main__':
    func_one()
    func_two()
    list_names()

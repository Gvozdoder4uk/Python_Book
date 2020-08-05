# Первое задание стр 42. Вывод преветственного сообщения
print("Задание №1")
my_name = "Олег"
my_lastname = " Фокин"
my_secondname = "Константинович "
my_fullname = f"{my_lastname} {my_name} {my_secondname}"
welcome_message = f"Приветствую {my_lastname.strip()} {my_name.strip()} {my_secondname.strip()}.\nПопрограмируем сегодня? "
print(welcome_message)

# Второе задание, вывод в различных регистрах
print("Задание №2")
print(my_fullname.lower().strip())
print(my_fullname.upper().strip())
print(my_fullname.title().strip())

# Третье задание.
print("Задание №3 и №4")
grand_message = "\tЕсть два способа разработки программного обеспечения. Первый — сделать ПО настолько простым, " \
                "чтобы в нём не было недостатков. \n\tВторой — сделать его настолько сложным, чтобы в нём не было очевидных " \
                f"недостатков. \n({my_fullname.title().strip()})"
print(grand_message)

famous_person = "Jeremy S. Anderson"
mega_message = f"\n\tДва самых известных продукта, созданных в Университете Беркли — это UNIX и LSD. \nЭто не может быть просто совпадением. ({famous_person})"
print(mega_message)
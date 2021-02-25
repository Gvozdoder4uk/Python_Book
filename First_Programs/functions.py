"""
Раздел разбирающий возможности и цель функций в PYTHON
"""


# Обьявление функции
def get_hello():
    print("Hello World")


# Вызов функции
get_hello()

username = "Олег"


def greetengs_users(username: list):
    for name in username:
        print(f"Привет {name}")


greetengs_users(username)
greetengs_users('Denis')
list  = ['Oleg', 'Kristy', 'Kate']
greetengs_users(list)
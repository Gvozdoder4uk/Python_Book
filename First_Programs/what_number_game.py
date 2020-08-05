import random

Try_counter = 0
print("Приветсвую тебя в твоей первой игре")
print("И так как тебя зовут?")
name = input()
print(f"И так {name.title()} сыграем в игру")
random_number = random.randint(1, 20)
print(f"{name.title()} я загадал число от 1 до 20.\n У тебя есть 3 попытки \nПопробуй отгадать:")

while Try_counter < 3:
    player_number = int(input())
    Try_counter += 1
    if player_number < random_number:
        print("Ты близок, но мое число немного больше твоего.")
    if player_number > random_number:
        print("И снова жарко, но мое число меньше.")
    if player_number==random_number:
        print("Потрясающе! Ты угадал!")
        break
if player_number != random_number:
    print(f"Увы ты проиграл попробуй снова! Загаданное число было {random_number}")


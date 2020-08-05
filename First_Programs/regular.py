import re

# В системе авторизации для секретной страницы есть правила: пароль должен начинаться с заглавной латинской буквы, состоять из латинских букв, цифр, и нижнего подчёркивания,
# но заканчиваться только латинской буквой или цифрой;
# минимальная длина логина — 8 символов, максимальная — 20.
# Напишите код, проверяющий соответствие входной строки этому правилу.
















patternpassword = re.compile("^[A-Z]*[_]*[a-zA-z0-9]{8,19}$")
print(bool(patternpassword.match('Zzzzzz1')))
print(bool(patternpassword.match('Zzzzzza_ф')))
print(bool(patternpassword.match('Zzzzzz123_№')))
print(bool(patternpassword.match('Zzzzzz_1')))
print(bool(patternpassword.match('Zzzzzz123_a')))
print(bool(patternpassword.match('Zzzzzz123_')))
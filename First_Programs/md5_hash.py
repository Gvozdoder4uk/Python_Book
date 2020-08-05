import string
import hashlib
import random


def randStr(chars=string.ascii_uppercase + string.digits, str_length=23):
    return ''.join(random.choice(chars) for _ in range(str_length))


def generateHashMd5(first_byte, str):
    str_hashed = bytes(str, 'utf-8')
    result = hashlib.md5(str_hashed)
    return result.hexdigest()


f_byte = '0a'
n = 0
while n == 0:
    my_str = randStr()
    my_hash = generateHashMd5(f_byte, my_str)
    if my_hash[0:2] != f_byte:
        pass
    else:
        n = 1
        print(f"{my_hash} и строка {my_str}")

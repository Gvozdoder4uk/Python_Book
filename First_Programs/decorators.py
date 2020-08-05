import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res

    return tmp


@timer
def func(x, y):
    result = list(range(2, x ** y, 2))
    return result


a = func(2, 5)
print(str(a))

import random


def random_list(size):
    lst = []
    n = size
    for i in range(size):
        r = random.randint(-10 * n, 10 * n)
        lst.append(r)
    return lst
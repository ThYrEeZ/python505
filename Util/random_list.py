import random


def random_list(size, number):
    lst = []
    for _ in range(number):
        lst.append(random.randint(-size, size))
    return lst

import random


def random_list(fron, to, number):
    lst = []
    for i in range(number):
        lst.append(random.randint(fron, to))
    return lst

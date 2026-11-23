import random


def random_list(start, stop, step, size):
    all_lists = []
    for n in range(start, stop + 1, step):
        lst = []
        for _ in range(n):
            lst.append(random.randint(-size, size))
        all_lists.append(lst)
    return all_lists

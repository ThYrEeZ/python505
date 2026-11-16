import time


def two_sum_brute(lst, n):
    result = set()
    for i in lst:
        for j in lst:
            if i + j == n:
                p = tuple(sorted((i, j)))
                result.add(p)
    return result


def two_sum_pointers(lst, n):
    result = set()
    lst = sorted(lst)
    fp = 0
    bp = len(lst) - 1
    while fp < bp:
        p = lst[fp] + lst[bp]
        if p == n:
            result.add(tuple((lst[fp], lst[bp])))
            fp += 1
        elif p > n:
            bp -= 1
        elif p < n:
            fp += 1
    return result


def two_sum_caching(lst, n):
    unique_pairs = set()
    cach = set()
    for v1 in lst:
        v2 = n - v1
        if v2 in cach:
            if v2 < v1:
                v1, v2 = v2, v1
            unique_pairs.add((v1, v2))
        cach.add(v1)
    return list(unique_pairs)


def time_taker(lst):
    x = time.time()
    two_sum_caching(lst, 5)
    timedifference = x - time.time()
    return timedifference


lst = [1, 19, 29, 11, 23, 10, 27, -3, -5, 19, -22, 28, -16, 9, -23]
print(time_taker(lst))

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
            result.add(p)
        elif p > n:
            bp -= 1
        elif p < n:
            fp += 1
    return result


lst = [1, 19, 29, 11, 23, 10, 27, -3, -5, 19, -22, 28, -16, 9, -23]
print(two_sum_pointers(lst, 5))

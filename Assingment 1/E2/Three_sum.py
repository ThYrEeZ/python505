def three_sum_brute(lst, n):
    result = set()
    for i in lst:
        for j in lst:
            for u in lst:
                p = i + j + u
                if p == n:
                    p = tuple(sorted((i, j, u)))
                    result.add(p)
    return result


def three_sum_pointers(lst, n):
    result = set()
    lst = sorted(lst)
    fp, bp = 1, len(lst) - 1

    for i in lst:
        while fp < bp:
            p = fp + bp
            if p == n:
                result.add(i + lst[fp] + lst[bp])
            elif p < 0:
                fp += 1
            elif p > 0:
                bp += 1
    return result


def three_sum_caching(lst, n):
    result = set()


lst = [1, 19, 29, 11, 23, 10, 27, -3, -5, 19, -22, 28, -16, 9, -23]
print(three_sum_brute(lst, 0))

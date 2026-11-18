import time



def three_sum_brute(lst, n):
    result = set()

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for u in range(j + 1, len(lst)):
                p = lst[i] + lst[j] + lst[u]
                if p == n:
                    p = tuple(sorted((lst[i], lst[j], lst[u])))
                    result.add(p)
    return result


def three_sum_pointers(lst, n):
    result = set()
    lst = sorted(lst)

    for i in range(len(lst)-2):
        fp, bp = i + 1, len(lst) - 1
        while fp < bp:
            p = lst[fp] + lst[bp] + lst[i]
            if p == n:
                result.add((lst[i], lst[fp], lst[bp]))
                fp += 1
            elif p < n:
                fp += 1
            elif p > n:
                bp -= 1
    return result


def three_sum_caching(lst, n):
    unique_pairs = set()

    for v1 in range(len(lst)-2):
        cach = set()
        for v2 in range(v1 + 1, len(lst)):
            v3 = n - lst[v1] - lst[v2]
            if v3 in cach:
                unique_pairs.add(tuple(sorted((lst[v1], lst[v2], v3))))
            cach.add(lst[v2])
    return unique_pairs

def time_test(function):

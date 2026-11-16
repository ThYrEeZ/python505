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


lst = [1, 19, 29, 11, 23, 10, 27, -3, -5, 19, -22, 28, -16, 9, -23]
print(three_sum_brute(lst, 0))

import Assignment_1.Util.random_list as random_list


def radix_sort(lst):
    if not lst:
        return lst
    # 1 hantera all negativa tal
    negatives = [-x for x in lst if x < 0]
    positives = [x for x in lst if x >= 0]
    # 2 sortering

    def radix_sort_positives(arr):
        if not lst:
            return lst
        max_value = max(arr)
        exp = 1
        while max_value // exp > 0:
            arr = sort_by_digit(arr, exp)
            exp *= 10
        return arr

    def sort_by_digit(arr, exp):
        # 3 set up buckets
        buckets = [[]for _ in range(10)]

        # 4 scatter
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        # 5 Gather
        new_lst = []
        for bucket in buckets:
            for num in bucket:
                new_lst.append(num)
        return new_lst

    sorted_negatives = radix_sort_positives(negatives)
    sorted_positives = radix_sort_positives(positives)

    return [-x for x in reversed(sorted_negatives)] + sorted_positives


print(radix_sort(random_list.random_list(100, 100)))

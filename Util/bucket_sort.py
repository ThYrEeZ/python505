import random_list


def bucket_sort(lst):
    if not lst:
        return lst
    # 1 set up buckets
    num_buckets = len(lst)
    buckets = [[]for _ in range(num_buckets)]

    # 2 scatter
    min_value, max_value = min(lst), max(lst)
    for value in lst:
        index = int((value - min_value) / (max_value - min_value + 1) * num_buckets)
        buckets[index].append(value)

    # 3 sort each bucket
    for bucket in buckets:
        bucket.sort()

    # 4 gather + return
    new_lst = []
    for bucket in buckets:
        for value in bucket:
            new_lst.append(value)
    return new_lst


print(bucket_sort(random_list.random_list(100, 100)))

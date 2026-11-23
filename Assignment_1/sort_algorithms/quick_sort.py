def quick_sort_slow(lst):
    if len(lst) == 0:
        return lst
    else:
        pivot, left, right = partition_slow(lst)
        sorted_left = quick_sort_slow(left)
        sorted_right = quick_sort_slow(right)
        return sorted_left + [pivot] + sorted_right


def partition_slow(lst):
    n = len(lst)
    pivot = lst[n - 1]
    left, right = [], []

    for i in range(n - 1):
        val = lst[i]
        if val < pivot:
            left += [val]
        else:
            right += [val]
    return pivot, left, right


def quick_sort_mean(lst):
    if len(lst) == 0:
        return lst
    else:
        pivot, left, right = partition_mean(lst)
        sorted_left = quick_sort_mean(left)
        sorted_right = quick_sort_mean(right)
        return sorted_left + [pivot] + sorted_right


def partition_mean(lst):
    n = len(lst)
    mean = sum(lst) / n
    left, right = [], []

    pivot_index = 0
    for i in range(n):
        if abs(lst[i] - mean) < abs(lst[pivot_index] - mean):
            pivot_index = i
    # Mäter avsvtådet från snitt för att se vilket element som är närmast
    # För att sedan använda det som det mellesta värdet.
    pivot = lst[pivot_index]

    for i in range(n):
        if i == pivot_index:
            continue  # skippar pivot
        val = lst[i]
        if val < pivot:
            left += [val]
        else:
            right += [val]
    return pivot, left, right

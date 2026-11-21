def merge_sort_slow(lst):
    if len(lst) > 1:
        first, last = 0, len(lst)
        mid = (first + last)//2  # Delar upp rekrusivt
        left = lst[first:mid]
        right = lst[mid:last]

        sortedleft = merge_sort_slow(left)
        sortedright = merge_sort_slow(right)

        sorted = merge_slow(sortedleft, sortedright)  # sickar ner alla listor
        return sorted
    else:
        return lst


def merge_slow(left, right):
    sorted = []
    i, j = 0, 0
    # detta är ett sätt att se vart den minsta är.

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted += [left[i]]
            i += 1  # kollar om båda inte tomma lägger till den ena
        else:
            sorted += [right[j]]
            j += 1

    while i < len(left):
        sorted += [left[i]]
        i += 1
# dessa kollar om någon av de andra är tomma och lägger till på sin plats
    while j < len(right):
        sorted += [right[j]]
        j += 1

    return sorted

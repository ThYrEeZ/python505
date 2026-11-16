def list_sum(lst):
    if lst == []:
        return 0

    value = lst[len(lst)-1]
    lst.pop(len(lst)-1)
    return value + list_sum(lst)


lst = [2, 2, 2, 2, 2, 3]
print(list_sum(lst))

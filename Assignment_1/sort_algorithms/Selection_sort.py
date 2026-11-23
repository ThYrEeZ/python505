def selction_sort(lst):
    n = len(lst)
    for i in range(n-1):
        index = i  # minsta änsålänge
        for j in range(i+1, n):
            if lst[j] < lst[index]:
                index = j  # Kollar allt förutom det vi redan kollar
                # och hittar det minsta bland de
        lst[i], lst[index] = lst[index], lst[i]  # Sätter mista på sin plats
    return lst

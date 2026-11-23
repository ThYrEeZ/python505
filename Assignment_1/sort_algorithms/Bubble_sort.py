def bubble_sort(lst):
    n = len(lst)-1
    for i in range(n):  # ytter loop
        swapped = False
        for j in range(n-i):
            if lst[j] > lst[j+1]:  # kollar rätt placering
                lst[j], lst[j+1] = lst[j+1], lst[j]  # byter plast
                swapped = True
        if not swapped:  # Med swapped vet jag när listan är sortead
            break
    return lst

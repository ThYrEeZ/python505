def is_pali(text):
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return is_pali(text[1:len(text)-1])
    else:
        return False

def is_pali(text):
    text = text.replace(" ","").lower()
    start = 0
    stop = len(text)-1
    return is_pali_rec(text,start,stop)

def is_pali_rec(text,start,stop):
    if (stop - start) <= 1:
        return True
    if text[start] == text[stop]:
        return is_pali_rec(text,start+1,stop-1)
    else:
        return False




print(is_pali("anna"))
print(is_pali("Anna"))
print(is_pali("racecar"))
print(is_pali("python"))
print(is_pali("Ni talar bra latin"))

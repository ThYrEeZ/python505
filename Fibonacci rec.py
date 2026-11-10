def fibr(n):
    if n == 0 or n==1:
        return n

    return fibr(n-1) + fibr(n-2)

for i in range(10):
    print(fibr(i))
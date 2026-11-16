def digit_sum(n):
    if n <= 9:
        return n

    x = n % 10

    return x + digit_sum(n//10)


print(digit_sum(99999))

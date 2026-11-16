def powerup(base, power):
    if power == 0 or base == 1:
        return base

    value = base * power
    power = power - 1
    return value + powerup(base, power)


print(powerup(2, 0))

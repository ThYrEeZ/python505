def lin_reg(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = sum(i * i for i in x)
    sxy = sum(x[i] * y[i] for i in range(n))
    denominator = n * sxx - sx ** 2
    intercept = (sxx * sy - sx * sxy) / denominator
    slope = (n * sxy - sx * sy) / denominator
    return intercept, slope

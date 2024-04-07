def sum_interval(a, b):
    if a > b:
        return 0  
    else:
        n = b - a + 1  
        return n * (a + b) // 2
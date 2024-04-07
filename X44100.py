def compress(n):
    n_str = str(n)
    result = n_str[0]
    
    for i in range(1, len(n_str)):
        # If the current digit is not the same as the previous one, add it to the result
        if n_str[i] != n_str[i - 1]:
            result += n_str[i]
    
    return int(result)


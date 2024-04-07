def compare_digits(p, q):
    p_str = str(p)
    q_str = str(q)
    
    freq_p = {}
    for digit in p_str:
        freq_p[digit] = freq_p.get(digit, 0) + 1     # Count the frequency of each digit in p
    
    freq_q = {}
    for digit in q_str:
        freq_q[digit] = freq_q.get(digit, 0) + 1     # Count the frequency of each digit in q

    for digit, count in freq_p.items():
        if digit not in freq_q or freq_q[digit] < count:     # Compare frequencies 
            return False
    
    return True


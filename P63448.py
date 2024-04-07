from pytokr import pytokr
item = pytokr()

def int_root(x):
    if x == 0 or x == 1:
        return x
    low = 0
    high = x // 2
    while low <= high:
        mid = (low + high) // 2
        mid_sq = mid * mid
        if mid_sq == x:
            return mid
        elif mid_sq < x:
            low = mid + 1
        else:
            high = mid - 1
    return high

while True:
    try:
        num = int(item())
        root = int_root(num)
        print(num, root)
    except:
        break

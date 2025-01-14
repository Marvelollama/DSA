def reverse(x: int) -> int:
    if x < 0:
        x = int(str(x)[::-1][:-1]) * (-1)
        if x < (-2) ** 31:
            return 0
    else:
        x = int(str(x)[::-1])
        if x > 2 ** 31:
            return 0
    return x
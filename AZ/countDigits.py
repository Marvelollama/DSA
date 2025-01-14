def evenlyDivides(n):
    num = str(n)
    count = 0
    for digit in num:
        if digit != '0' and n % int(digit) == 0:
            count += 1
    return count
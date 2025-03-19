def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a + b + c


def fix_teen(n):
    if n != 15 and n != 16 and 13 <= n <= 19:
        return 0
    return n
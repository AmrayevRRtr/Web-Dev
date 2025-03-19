a = input().strip()
pow = 0
res = 0

for i in a[::-1]:
    i = int(i)
    res += i * (2**pow)
    pow += 1

print(res)


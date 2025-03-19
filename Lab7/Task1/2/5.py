# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = {}

words = [input() for _ in range(n)]

for word in words:
    if (word not in s):
        s[word] = 0
    s[word] += 1

print(len(s))
for value in s.values():
    print(value, end=" ")





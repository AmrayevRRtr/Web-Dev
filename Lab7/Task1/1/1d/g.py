n = int(input())
arr = list(map(int, input().split()))[:n]

print(*arr[::-1])
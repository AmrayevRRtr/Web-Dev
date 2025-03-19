import sys

n = int(input())
arr = list(map(int, input().split()))[:n]

for i in range(1, n):
    if(arr[i-1] < 0 and arr[i] < 0 or arr[i-1] >= 0 and arr[i] >= 0):
        print("YES")
        sys.exit()


print("NO")
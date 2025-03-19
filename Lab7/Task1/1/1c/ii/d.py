import sys

a = int(input())
s = 1

while(s <= a):
    if(s == a):
        print("YES")
        sys.exit()
    s = s * 2

print("NO")
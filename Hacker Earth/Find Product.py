import math as m
n = int(input())
myarr = list(map(int,input().split()))

ans = 1
for i in myarr:
    ans = (ans*i) % (m.pow(10,9)+7)
print(int(ans))

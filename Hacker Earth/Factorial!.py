import math
n = int(input())

ans = 1
for i in range(1,n+1):
    ans*=i
print(ans)
print(math.factorial(n))
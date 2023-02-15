l,r,k = map(int,input().split())

ans = 0
for i in range(l,r+1):
    if i%k==0:
        ans+=1
print(ans)

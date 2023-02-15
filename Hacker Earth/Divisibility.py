n = int(input())
arr = list(map(int,input().split()))
data = ""
for i in arr:
    a=i%10
    data+=str(a)

data=int(data)
if data%10 ==0:
    print("Yes")
else:
    print("No")


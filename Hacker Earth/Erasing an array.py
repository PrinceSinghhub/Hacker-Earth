n=int(input())

for i in range(n):
    ar=int(input())
    el=list(map(int,input().split()))
    count=1


    for j in range(1,ar):
        if el[j] < el[j-1]:
            count=count+1
    print(count)
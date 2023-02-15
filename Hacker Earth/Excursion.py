for _ in range(int(input())):

    [n,m,k]=list(map(int,input().split()))

    total=0

    while n>0:

        total+=1

        n-=k

    while m>0:

        total+=1

        m-=k

    print(total)
from math import floor

T = int(input())

while (T):

    N,K = input().split()

    N = int(N)

    s = sum(list(map(int,input().split())))

    K = int(K)

    x = floor( s/(K+1) - N + 1 )

    print(max(x, 0))

    T-=1


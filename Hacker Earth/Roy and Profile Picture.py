# L = int(input())
# N = int(input())

# for i in range(N):
#     W,H = map(int,input().split())
#     if W == H:
#         print("ACCEPTED")

#     if W<L or H<L:
#         print("UPLOAD ANOTHER")

#     if W>L and H>L:
#         print("CROP IT")

L = int(input())
N = int(input())
while N !=0 :
    T = list(map(int, input().split()))
    W = T[0]
    H = T[1]
    if L>W :
        print("UPLOAD ANOTHER")
    elif L>H:
        print("UPLOAD ANOTHER")
    elif H == W :
        print("ACCEPTED")
    else:
        print("CROP IT")
    N = N-1
T= int(input())

for a in range(T):
    g,p=[int(x) for x in input().split()]
    (sum1,sum2)=(0,0)
    num=int(input())
    for i in range(num):
        m,n= [int(j) for j in input().split()]

        sum1= (m*g+n*p)+sum1

        sum2= (m*p+n*g)+sum2

    print(min(sum1,sum2))
n=int(input())

for i in range(0,10):
    x,y=(input().split())
    x=int(x)
    l=[]
    for o in range(0,x):
        s=input()
        k=s.count("#")
        l.append(k)
    print(max(l))
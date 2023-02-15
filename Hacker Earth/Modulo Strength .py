d={}

k = int(input().split()[1])

l = [int(i) for i in input().split()]

for i in l:

     try: d[i%k] += 1

     except: d[i%k] = 1

print(sum(d[i] * (d[i]-1) for i in d))
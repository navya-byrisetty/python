n,m=map(int,input().split())
c=[0]*m
for i in range(n):
    row=list(map(int,input().split()))
    for j in range(m):
        c[j]+=row[j]
for s in c:
    print(s)

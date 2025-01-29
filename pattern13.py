n=int(input())
t=[[1]]
for i in range(1,n):
    r=[1]*(i+1)
    for j in range(1,i):
        r[j]=t[i-1][j-1]+t[i-1][j]
    t.append(r)
for r in t:
    print(" ".join(map(str,r)))

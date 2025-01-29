n=int(input())
for i in range(1,n+1):
    ip=[chr(65+j) for j in range(i)]
    dp=ip[:-1][::-1]
    p=ip+dp
    print(" ".join(p))

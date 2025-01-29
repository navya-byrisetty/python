a=int(input())
for v in range(a):
    val=v+1
    dec=a-1
    for j in range(v+1):
        print(val,end=" ")
        val=val+dec
        dec=dec-1
    print()

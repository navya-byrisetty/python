a=int(input())
for i in range(a):
    for j in range(a,i+1,-1):
        print(j,end='')
    print("*",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
        

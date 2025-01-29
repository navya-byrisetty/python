a=int(input())
for i in range(a):
    for j in range(a-i):
        if(i==0 or j==0 or j==a-i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

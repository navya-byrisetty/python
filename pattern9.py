a=int(input())
num=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
        num+=1
    print()
for i in range(a-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    

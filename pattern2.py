a,b=map(int,input().split())
for i in range(b):
    if(i==0 or i==b-1):
        print("*"*a)
    else:
        print("*"+" "*(a-2)+"*")
    

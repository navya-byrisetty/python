num=int(input("a is "))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime")
    
def prime(a):
    flag=False
    for i in range(1,a+1):
        if(a%i==0):
           flag=True
           break
    if(flag):
        print("not A prime")
    else:
        print("prime")
a=int(input())
result=prime(a)

print("}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}:")

a=0
b=1
for i in range(2,10):
    s=a+b
    a=b
    b=s
    print(s)
    
print("using functions")

def fibnoci(a,b):
    for i in range(2,30):
        s=a+b
        a=b
        b=s
        print(s,end=" ")
a=0
b=1
result=fibnoci(a,b)

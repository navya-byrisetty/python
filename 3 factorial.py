num=int(input("enter a number:"))
fact=1
if(num<0):
    print("doesnot exist")
elif(num==0 or num==1):
    print(f"factorial of {num} is 1")
else:
    for i in range(1,num+1):
        fact*=i
    print(f"factorial of { num} is: {fact}")

print("|||||||||||||||||||||||||||||||||||||||||||")
print("using functions")

def fact(num):
    fact=1
    if (num<0):
        print("doesnot exit")
    elif(num==0 or num==1):
        print("factorial is 1")
    else:
        for i in range(1,num+1):
            fact*=i
        print(fact)
num=int(input("a is :"))
result=fact(num)



print("{{{{{{{{{{{{{{{{{{{{")
print("using recursion")
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
num=7
print(fact(num))

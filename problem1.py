a=int(input("enter the bill"))
t=int(input("what percentage tip would u like "))
p=int(input("how many people to split the the bill"))
b=t/100
s=a*b
total=a+s
bill=total/p
print(bill)

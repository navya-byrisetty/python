num1=10
num2=20
print("before swapping two numbers",num1,num2)
temp=num1
num1=num2
num2=temp
print("ater swapping two nubers ",num1,num2)

print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

print("second apporach")
print("]]]]]]]]]]]]]]]]]]]]]]]]]")

a=10
b=29
a,b=b,a
print(a,b)

print("==============================+++++++++++")
print("3 approch")
a=10
b=39
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)

print(".>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("using functions")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
def swap(a,b):
    a,b=b,a
    print(a,b)
a=10
b=20
result=swap(a,b)


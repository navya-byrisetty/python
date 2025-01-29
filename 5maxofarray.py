arr=[8,9,6,88,55]
max=arr[0]
n=len(arr)
for i in range(1,n):
    if(arr[i]>max):
        max=arr[i]
print(max)

print("/???????????????")
print("using fuction to find the minimum number in an array")



def smallest(arr):
    min=arr[0]
    n=len(arr)
    for i in range(1,n):
        if(arr[i]<min):
            min=arr[i]
    print(min)
arr=[23,11,3,43,56,1,2,77,190,55,66,99,22,121]
result=smallest(arr)

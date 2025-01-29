numbers=input("enter numbers: ")
numbers_list=numbers.split(",")
count=0
for number in numbers_list:
    count+=1
print("length of the list:",count)
for i in range(count):
    numbers_list[i]=int(numbers_list[i])
maximum_number=numbers_list[0]
for number in numbers_list:
    if(number>maximum_number):
        maximum_number=number
print("maximum num is",maximum_number)
total=0
for i in range(0,101,1):
    if(i%3==0  and i%5==0):
        print("FIZZBuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print(i)
		

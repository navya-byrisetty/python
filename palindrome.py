str1="madama"
n=len(str1)
rev=""
for i in range(n-1,-1,-1):
    rev=rev+str1[i]
print(rev)
if(rev==str1):
    print("palindrome")
else:
    print("not palindrome")

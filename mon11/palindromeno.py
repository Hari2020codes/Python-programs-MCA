# checking if a number is palindrome
n=int(input("Enter a number: "))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print(temp, "is a Palindrome number")
else:
    print(f"{temp} is not a Palindrome number")    
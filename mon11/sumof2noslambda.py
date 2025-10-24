# to find sum of two numbers using lambda function
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=lambda x,y:x+y
print(f"The sum of {num1} and {num2} is {sum(num1,num2)}")
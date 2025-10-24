# to find sum of numbers from 1 to n using recursion
def sumofn(n):
    if n == 1:
        return 1
    else:
        return n + sumofn(n - 1)
num = int(input("Enter a number to find the sum from 1 to n: "))
result = sumofn(num)
print(f"The sum of numbers from 1 to {num} is {result}")
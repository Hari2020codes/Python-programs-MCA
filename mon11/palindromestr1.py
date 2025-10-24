# to check if a string is palindrome or not using slicing []
s=input("Enter a string: ")
rev=s[::-1]
if s==rev:
    print(f'"{s}" is a Palindrome string')
else:
    print(f'"{s}" is not a Palindrome string')

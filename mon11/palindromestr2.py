# to check id a string is palindrome or not
s=input("Enter a string: ")
rev=""
for char in s:
    rev=char+rev

if s==rev:
    print(f'"{s}" is a Palindrome string')  
else:
    print(f'"{s}" is not a Palindrome string')
    
# fibonacci numbers of n terms
n=int(input("enter the number"));
a=0;b=1;c=0;
for i in range(n+1):
    a=b;
    b=c;
    c=a+b;
    print(c)
    

n=int(input("enter the number :"))
s=0
while(n>0):
    d=n%10
    s=s+d
    n//=10
print(s)    


    
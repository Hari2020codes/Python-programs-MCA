# factorial of a number
num=int(input("enter a no: "));
if(num<0):
    
  print("factorial doesn't exist for negative numbers")
    
elif(num==0):
   
  print("factorial of 0 : 1")
    
else:        
 
     fact=1;
     for i in range(1,num+1):
       
       fact=fact*i;
     print("factorial of ",num,"is:",fact) 
    
 
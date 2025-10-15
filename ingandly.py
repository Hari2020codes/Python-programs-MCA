#add ing or ly to end of string
str=input("enter the str: ")
if(len(str)>2):
    if(str[-3:]=='ing'):
        str=str+'ly'
    else: 
       str= str+'ing'  
        
else:
    print("invalid length")        
print(str)        
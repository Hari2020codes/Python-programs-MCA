str=input("enter the string: ");
count=0
for i in range(len(str)):
    if((str[i]=='a')or(str[i]=='e')or(str[i]=='i')or(str[i]=='o')or(str[i]=='u')):
        print(str[i])
        count+=1
print("no: vowels:", count)        
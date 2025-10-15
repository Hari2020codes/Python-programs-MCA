# to print no: vowels in a string
# to count no: characters in a string
str=input("enter the str :")

count=0
for i in range(len(str)):
  if((str[i]=='a')or(str[i]=='e')or(str[i]=='i')or(str[i]=='o')or(str[i]=='u')):
    count+=1
print(count)    
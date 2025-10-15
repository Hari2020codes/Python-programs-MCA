# prog to swap first letter of 2 string USING SLICE
str1=input("enter first string ");
str2=input("enter second string ");

new_str1 = str2[0] + str1[1:]
new_str2 = str1[0] + str2[1:]
print(new_str1+" "+new_str2)

# USING REPLACE()
str3=str1.replace(str1[0],str2[0])
str4=str2.replace(str2[0],str1[0])
print(str3+" "+str4)
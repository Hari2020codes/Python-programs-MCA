
list1=list(map(int, input("enter nos ").split(",")))

print("the list is : ", list1)

list2=[]

for i in list1:
    if(i%2==0):
        continue;
    list2.append(i)
print("the list of odd nos :", list2)        
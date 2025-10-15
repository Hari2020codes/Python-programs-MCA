
list1=list(map(int, input("enter nos ").split(",")))

print("the list is : ", list1)

list2=[]

for x in list1:
    if(x%2==0):
        list2.append(x)
print("the list of even nos :", list2)        
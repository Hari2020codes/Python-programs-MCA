clist1=input("enter colours of list1:").split(",");
clist2=input("enter colours of list2:").split(",");
setclist1=set(clist1)
setclist2=set(clist2)
diffclist1=setclist1.difference(setclist2)
print(diffclist1)
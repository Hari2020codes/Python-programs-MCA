list1=[1,2,3,4];
print(list1);
l2=list1[1:2];         
print(l2);
l2=list1[1:-1];
print(l2);
  #print twice
  
print(list1*2)
# concat
list2=[5,6,7,8]
print(list1+list2)
# length
print(len(list1))
#max,min
print(max(list1),min(list1))
#append
list1.append(1)
print(list1)
# count repeatetion
print(list1.count(1))
# remove
list1.remove(1)
print(list1)
# insert element at an index
list1.insert(5,1)
print(list1)
# sort a list    
list1.sort()
print(list1)

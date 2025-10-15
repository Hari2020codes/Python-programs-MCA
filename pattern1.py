#1 print 4* in 4 rows
for i in range(4):
    print('*'*4)
    
#2 print 1to4 * in each rows respectively
# *
# **
print()
for i in range(1,4):
    print('*'*i)
#OR
            
for i in range(4):
    for j in range(i):
        print('*', end=" ")
    print()  # moves to the next line after each inner loop                 
        
#3 print 4to1 * in each rows respectively
# ****
# ***
print()
for i in range(4,0,-1):
    print('*'*i)
                
#4 print pattern 
# 1
# 22
# 333
for i in range(4):
    for j in range(i):
        print(i, end=" ")
    print()  # moves to the next line after each inner loop

for i in range(10):
    for j in range(i):
        print(j, end=" ")
    print()  # moves to the next line after each inner loop
    
 
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#  ***************************************   
for i in range(5,0,-1):
    for j in range(6,i,-1):
        print(i,end=" ")
    print()
    
# **************
for i in range(5,0,-1):
    for j in range(6,i,-1):
        if j % 2 == 0:
            print("0",end=" ")
        else:
            print("1",end=" ")    
    print()    
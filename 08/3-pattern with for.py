# chaop jadval zarb
# for i in range (1,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")
#     print()

# cde 2
# for i in range (1,10):
#     for j in range(1,10):
#         if i % 2 == 0 and j %2 == 0:
#             print(f"{i} * {j} = {i*j}")
#     print()
#     
# pattern -->  1 1 1 1 1    
# for i in range(6):
#   print(1,end=" ")
#   
# """ patern
# 1
# 1
# 1
# 1
# 1
# """
# for i in range(6):
#   print(1,end="\n")
#   
# pattern 1 2 3 4 5
# for i in range(6):
#     print(i,end=" ")
""" patern -->
1
2
3
4
56
"""
# for j in range (6):
#     print(j)
#     
for i in range(2):
    for j in range(6):
        print(j,end=" ")
    print()
    
for i in range(6):
    for j in range(2):
        print(i,end=" ")
    print()    
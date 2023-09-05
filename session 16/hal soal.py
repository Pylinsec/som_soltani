colors = ['red','blue','green','red','yellow','red']

# revesh avval
# red_count =colors.count('red')
# for item in range(red_count):
#     colors.remove('red')
# print(colors)

# revesh dovom
print(colors.index('red'))
for item in colors:
    index_1 = colors.index('red')
    colors.pop(index_1)

print(colors)    
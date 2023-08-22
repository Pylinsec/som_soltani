colors = ['red','green','blue','yellow','black']
colors2 = colors
# print(colors2)

# colors.append('som')
# print(colors2)

# colors.clear()
# print(colors2)

colors3 = colors.copy()
colors.pop()
colors.insert(2,'soltani')
print(colors)
print(colors3)



# estefadeh az loop ya for dar list
colors = ['red','green','blue','yellow','black']
# for item in colors:
#     print(item)

for i in colors:
    if i == 'blue':
        # break
        continue
    print(i)

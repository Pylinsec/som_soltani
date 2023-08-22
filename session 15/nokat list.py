l1 = [1,2]
l1.extend('somsoltani')
print(l1)

# remove(item)
# 1--> hazf item khas
colors = ['red','green','blue','yellow','black']
# colors.remove('red')
print(colors)
# 2--> pop() hazf ba index
# colors.pop() # dar insoortat az tehe list hazf mikonad
# colors.pop()
# colors.pop()
# print(colors)
colors.pop(1) # hazf item bar asas index ya shomareh khaneh 
print(colors)
# clear()--> hazf temam item ha 
colors.clear()
print(colors)

# del
del colors
print(colors)
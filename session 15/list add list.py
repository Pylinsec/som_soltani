colors = ['red','green','blue','yellow','black']
cars = ['pride','benz','traktor']

newlist = colors + cars
print(newlist)
# extend --. list1.extend(list2)
# colors.extend(cars)
# print(colors)
cars.extend(colors)
print(cars)

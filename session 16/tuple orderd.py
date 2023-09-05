
#  yani chi ke tuple orderd hast
num = (1,2)
num2 = (2,1)
print(num is num2)


# changeable 
# rahehal change in tuple
#1- list(num)
#2- changes
#3- tuple(num)

# mesal
numbers = (10,20,30,40,50)
print(numbers)
new_list = list(numbers) # tabdil tuple be list ba constructor list
new_list.remove(30)
numbers = tuple(new_list) # tabdil list be tuple ba constructor tuple
print(numbers)
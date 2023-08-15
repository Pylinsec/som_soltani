#  list --> [] --> orderd , changeable , allow duplicate
#  mesal
[1,2,4] # list adadi
['som','soltani'] # list string 
[True,False] # list boolean
[1,'som',False,3.54,['som',]]# mix az hamechiz 

# ordere --> jaye item ha mohem hast yani 
print([1,2]==[2,1]) # 1 --> shomarekhane 0 , 1 ,shomareh kbhane 1

# changeable --< beryae ma emdkan taggir item ha hast 
adad = [1,2]
adad[0]='som'
print(adad)
# allow duplicate -->  tekrar mipezirad 
colors = ['red','red','red']
print(colors)


# type()
print(type(colors))


# len() --> jehat bedast avardan tool list
print(f'tedad item ha ={len(colors)}')

# chetoor az string list besazim  --> list()--> constructor
name = 'som soltani'
name_list = list(name)
print(name_list)

print(str(name_list))
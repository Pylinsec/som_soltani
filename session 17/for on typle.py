colors = ('red','blue','yellow','black','white','red','aqua')

# loop 1 
for item in colors:
    # print(item.capitalize())
    print(item.title())
    # print(item.upper())

# fpr noe 2 ba range
lenght = len(colors)
# print("tool tuple colors ast : ",lenght)
for i in range(lenght):
    # print(i)
    # f'harchizi ke benevis chap mikone {i}'
    print(f"{i}===> {colors[i]} ")


#  mesal --> bedast avardan majmooe adadha yek tuple 
num = (1,2,-888,34434,578,44,4,56,67)
sum=0
for item in num:
    sum += item
    print(sum)
print(sum)    

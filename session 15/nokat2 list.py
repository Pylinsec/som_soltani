# method
colors = ['red','green','green','yellow','black','geren']
# count()
print(colors.count('green')) # tedad item dadeh shodeh ra mishomarad

# index() --> shomareh khane barmigardand 
print(colors.index('green'))

# reverse()--> az akhar be aval list tagir mideh 
colors.reverse()
print(colors)

# sort()  --> bayad list ma ya string bashe ya hame adad bashand
colors.sort(reverse=True)
print(colors)

# adad 
number = [1,4,-3,555]
number.sort(reverse=True)
print(number)
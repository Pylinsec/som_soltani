name = 'som soltai from shahrak'
# sefah jehat yadavri
# split
l1 = name.split()
print(l1)
l1 = name.split(maxsplit=2) # feghat 2 ta space miad tabdil mikone
print(l1)
name = 'som*soltai*from*shahrak'
l1 = name.split(maxsplit=20 ,sep='*')
print(l1)
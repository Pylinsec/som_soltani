# string methods --> heman tabe khodemani
name1 = 'som soltani'
name2 = 'SOOAAOOOOOM'
name3 = 'SoM'

# capitalize() --> harf aval az avalin word jomleh ra capital mikonad
print(name1.capitalize())
print(name3.swapcase()) # koochik be bozorg , va bozorg be koochik
# title() --> avalin harf temam kelemat jomleh ra capital mikond 
print(name1.title())

# casefold() or lower() --> convert capital to lower
print(name2.lower())
print(name2.casefold())

# upper() --> convert small char to capital char
print(name1.upper())

# index(chiz), find(chiz) --> bargardandan shomare khane chiz
print(name1.index('s'))
print(name1.find('s'))
# print(name1.index('3')) # agar chiz nebashad dar string error mide 
print(name1.find('3')) # vaghti ke chiz nebashad -1 ra return mikonad

# center(adad,'chiz por kon') --. agar tedad char string ma za adad koochaktar bood hichi agar nebood ba chiz por kon
print('='.center(120,'='))
print('-'.center(120,'-'))
print('som soltani'.center(120,'*'))
print('-'.center(120,'-'))
print('='.center(120,'='))

# count(chiz) --> chiz mishomarad
print(name2.count('O'))

# replace('chiz1','chiz2')
print(name2.replace('O','qoli'))

# strip , split , join

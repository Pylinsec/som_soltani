# shorthand if
# tamerin even and odd(zoj or fard)
num = 44
if num % 2 == 0:
    print('even')
else:
    print('odd')
print('even')if num % 2 == 0 else print('odd')

# negetive and positive
print('negetive') if num < 0 else print('zero') if num == 0 else print('positive')
if num < 0:
    print('negetive')
elif num == 0:
    print('zero')
else:
    print('positive')
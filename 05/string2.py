#string


'''
# in , not in
print('q' in name)
print('q' not in name)
'''
name = "som soltani in class python course"
# string slicing  be mani tike tike kardan --> string[start:end:step]
# pattern 1  [a:b] from a to b-1   yani khode b jozv on nist
print(name[0:5:1]) # az index 0 ta index 5 yeki yeki 
print(name[:5]) # az avval to index 4
print(name[1:]) # az index 1 to akhar 
print(name[1::2]) #az index 1 ta akhar 2 ta 2 ta
print(name[::]) # az avval ta akhasr

# nokteh mohom::: keran bala dar soorat vojod joz index nist name[a:b] --> az index a to index b-1
'''
print(name[4:7])
print(name[::-1]) # reverse string barmigardand  yani makoos
print(name[-6:-1]) #  index -6 yani khane 6 az rast  
print(name[-6:-1:3])
print(name[:-6]) # az avval yani index -5
print(name[-10:-3:5]) # az index -10 ta index -3  5 ta  ta

#print(name[-10:-1:-1]) # in emkanpazir nis rahehal paeiin
name1 = name[-10:-1]
print(name1)
print(name1[::-1]) # makoos ya az rast index avval bezar va yeki yeki be chap boro
print(name[::-3]) # az rast index aval bezar va 3 ta 3 ta be samt chap

'''

name1 = "som soltani"
print(type(name1))
print(len(name1))  
print(name1[0:11])# in addad  az 0 hast ta len(name1) -1




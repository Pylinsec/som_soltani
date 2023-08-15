#max maximum   3 addad begirim bozorgtarin chap konad ba IF 
#min minimum  3 addad begirim kochektarin chap konad ba IF
a = int(input("insert first number a:"))
b = int(input("insert first number b:"))
c = int(input("insert first number c:"))
print(f"a={a},b={b},c={c}")

# revesh avval ba if , else if
print("*********************** revesh avval with if, else*********************")
if a > b:
    max1 = a
    if max1 > c:
        print(f"max={max1}")
    else:
        print(f"max={c}")
else:
    max1 = b
    if max1 > c:
        print(f"max={max1}")
    else:
        print(f"max={c}")
#revesh hal ba if , elif , else
print("*********************** revesh dovom ba elif*********************")
if a > b : # true
    if a >c: # true 
        print(a)
    else:
        print(c)
elif b > c:
    print(b)
else:
    print(c)

#revesh sevvom
print("*********************** revesh sevvom ba tabe max*********************")
print(max(a,b,c))   
          
             
